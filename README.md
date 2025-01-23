# 미국 자전거 공유 데이터 분석

이 프로그램은 미국의 자전거 공유 데이터를 분석하여 사용자가 선택한 도시, 월, 요일에 대한 통계를 제공한다.

## 소개
이 프로그램은 사용자가 입력한 도시, 월, 요일에 따라 자전거 공유 데이터를 필터링하고, 다양한 통계를 계산하여 출력한다.

## 사용 방법
1. 프로그램을 실행합니다.
2. 분석할 도시 이름을 입력합니다. (예: `chicago`, `new york city`, `washington`)
3. 필터링할 월을 입력합니다. (예: `all`, `january`, `february` ...)
4. 필터링할 요일을 입력합니다. (예: `all`, `monday`, `tuesday` ...)
5. 통계 결과를 확인합니다.
6. 원시 데이터를 5행씩 추가로 볼 수 있다.
7. 프로그램을 다시 실행할지 여부를 선택한다.

## 기능

### 시간 통계
- 가장 흔한 월, 요일, 시간을 계산하여 출력한다.

### 역 통계
- 가장 인기 있는 출발지, 도착지 및 여행 경로를 출력한다.

### 여행 시간 통계
- 총 여행 시간과 평균 여행 시간을 계산하여 출력한다.

### 사용자 통계
- 사용자 유형, 성별 및 출생 연도 통계를 출력한다.

### 원시 데이터 표시
- 사용자가 요청할 경우 원시 데이터를 5행씩 출력한다.

## 코드 설명

### 주요 함수
- `get_filters()`: 사용자로부터 도시, 월, 요일을 입력받습니다.
- `input_valid_option(prompt, valid_options)`: 유효한 옵션을 입력받습니다.
- `load_data(city, month, day)`: 지정된 도시 데이터를 로드하고 필터링합니다.
- `calculate_mode(series, description)`: 주어진 Series에서 가장 빈도 높은 값을 반환합니다.
- `time_stats(df)`: 가장 빈번한 여행 시간에 대한 통계를 계산하고 출력합니다.
- `station_stats(df)`: 가장 인기 있는 출발지와 도착지, 여행 경로를 출력합니다.
- `trip_duration_stats(df)`: 총 여행 시간과 평균 여행 시간을 출력합니다.
- `format_time(seconds)`: 초를 시, 분, 초 형식으로 변환합니다.
- `user_stats(df)`: 사용자 유형, 성별, 출생 연도 통계를 출력합니다.
- `display_raw_data(df)`: 원시 데이터를 5행씩 출력합니다.
- `main()`: 프로그램 실행의 메인 함수입니다.

이 프로그램은 Pandas 라이브러리를 사용하여 데이터를 처리하며, CSV 파일에서 데이터를 로드합니다. 사용자에게 친숙한 인터페이스를 제공하여 쉽게 데이터를 분석할 수 있도록 설계되었다.