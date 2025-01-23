import time
import pandas as pd
import numpy as np

# 도시 이름과 데이터 파일 경로 매핑
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    사용자로부터 분석할 도시, 월, 요일을 입력받습니다.

    Returns:
        city (str): 분석할 도시 이름
        month (str): 필터링할 월 이름 또는 "all" (모든 월)
        day (str): 필터링할 요일 이름 또는 "all" (모든 요일)
    """
    print('안녕하세요! 미국 자전거 공유 데이터를 탐색해봅시다!')

    city = input_valid_option("분석할 도시 이름을 입력하세요", list(CITY_DATA.keys()))
    month = input_valid_option("필터링할 월을 입력하세요 (예: 'all', 'january' ... 'december')", 
                               ['all'] + [m.lower() for m in pd.date_range('2023-01', '2024-01', freq='M').strftime('%B')])
    day = input_valid_option("필터링할 요일을 입력하세요 (예: 'all', 'monday' ... 'sunday')", 
                             ['all'] + [d.lower() for d in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']])

    print(f"\n입력한 값 - 도시: '{city}', 월: '{month}', 요일: '{day}'")
    print('-' * 40)

    return city, month, day

def input_valid_option(prompt, valid_options):
    """
    사용자로부터 유효한 옵션을 입력받습니다.

    Args:
        prompt (str): 입력 요청 메시지
        valid_options (list): 유효한 입력 값 목록

    Returns:
        str: 사용자 입력 값
    """
    while True:
        user_input = input(f"{prompt} {valid_options}: ").lower()
        if user_input in valid_options:
            return user_input
        print("잘못된 입력입니다. 다시 시도해주세요.")

def load_data(city, month, day):
    """
    지정된 도시 데이터를 로드하고 필터링합니다.

    Args:
        city (str): 도시 이름
        month (str): 필터링할 월 이름 또는 "all"
        day (str): 필터링할 요일 이름 또는 "all"

    Returns:
        DataFrame: 필터링된 데이터
    """
    df = pd.read_csv(CITY_DATA[city])

    # 'Start Time' 컬럼을 datetime 형식으로 변환
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day'] == day]

    return df

def calculate_mode(series, description):
    """주어진 Series에서 가장 빈도 높은 값을 반환합니다."""
    return series.mode()[0] if not series.empty else f"{description} 데이터를 찾을 수 없습니다."

def time_stats(df):
    """가장 빈번한 여행 시간에 대한 통계를 계산하고 출력합니다."""
    print('\n가장 빈번한 여행 시간 통계를 계산 중입니다...\n')

    common_month = calculate_mode(df['Month'], "월")
    common_day = calculate_mode(df['Day'], "요일")
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = calculate_mode(df['Hour'], "시간")

    print(f"가장 흔한 월: {common_month}")
    print(f"가장 흔한 요일: {common_day}")
    print(f"가장 흔한 시간: {common_hour}시")
    print('-' * 40)

def station_stats(df):
    """가장 인기 있는 출발지와 도착지, 여행 경로를 출력합니다."""
    print('\n가장 인기 있는 역 통계를 계산 중입니다...\n')

    common_start_station = calculate_mode(df['Start Station'], "출발지")
    common_end_station = calculate_mode(df['End Station'], "도착지")
    common_route = calculate_mode(df['Start Station'] + " -> " + df['End Station'], "경로")

    print(f"가장 많이 사용된 출발지: {common_start_station}")
    print(f"가장 많이 사용된 도착지: {common_end_station}")
    print(f"가장 빈번한 경로: {common_route}")
    print('-' * 40)

def trip_duration_stats(df):
    """총 여행 시간과 평균 여행 시간을 출력합니다."""
    print('\n여행 시간 통계를 계산 중입니다...\n')

    total_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()

    print(f"총 여행 시간: {format_time(total_time)}")
    print(f"평균 여행 시간: {format_time(mean_time)}")
    print('-' * 40)

def format_time(seconds):
    """초를 시, 분, 초 형식으로 변환합니다."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = round(seconds % 60, 2)
    return f"{hours}시간 {minutes}분 {seconds}초"

def user_stats(df):
    """사용자 유형, 성별, 출생 연도 통계를 출력합니다."""
    print('\n사용자 통계를 계산 중입니다...\n')

    print("사용자 유형:")
    print(df['User Type'].value_counts(), '\n')

    if 'Gender' in df.columns:
        print("성별:")
        print(df['Gender'].value_counts(), '\n')
    else:
        print("성별 데이터가 없습니다.\n")

    if 'Birth Year' in df.columns:
        print(f"가장 오래된 출생 연도: {int(df['Birth Year'].min())}")
        print(f"가장 최근 출생 연도: {int(df['Birth Year'].max())}")
        print(f"가장 흔한 출생 연도: {int(df['Birth Year'].mode()[0])}")
    else:
        print("출생 연도 데이터가 없습니다.")

    print('-' * 40)

def display_raw_data(df):
    """사용자 요청에 따라 원시 데이터를 5행씩 출력합니다."""
    start_row = 0
    while True:
        user_input = input("\n원시 데이터를 5행씩 더 보시겠습니까? 'yes' 또는 'no': ").lower()
        if user_input == 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row += 5
            if start_row >= len(df):
                print("\n더 이상 데이터가 없습니다.")
                break
        elif user_input == 'no':
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

def main():
    """프로그램 실행의 메인 함수."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("입력한 조건에 맞는 데이터가 없습니다.")
        else:
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        if input('\n다시 실행하시겠습니까? "yes" 또는 "no": ').lower() != 'yes':
            print("프로그램을 종료합니다. 감사합니다!")
            break

if __name__ == "__main__":
    main()