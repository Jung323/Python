import pandas as pd
# 1) 날짜 생성

# 인덱스 범위 지정만이 목적
# 시작 날짜와 끝 날짜를 지정해 데이터를 생성. 하루씩 증가한 날짜 데이터가 생성된다.
print(pd.date_range(start='2024-01-13',end='2024-01-31'))

# 결과:
# DatetimeIndex(['2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16',
#                '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20',
#                '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24',
#                '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28',
#                '2024-01-29', '2024-01-30', '2024-01-31'],

# 날짜 데이터를 입력할 때 yyyy-mm-dd형식이 아니라
# yyyy/mm/dd,yyyy.mm.dd,mm/dd/yyyy 같은 형식 모두 사용 가능
# 대신 출력은 yyyy-mm-dd형식으로 출력

print(pd.date_range(start='2024/01/01',end='2024.1.13'))

print(pd.date_range(start='01-01-2024',periods=7))
# periods=n : n개의 날짜 추가
# 결과:
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
#                '2024-01-05', '2024-01-06', '2024-01-07'],
#               dtype='datetime64[ns]', freq='D')


# 약어    설명    사용    예
#  D       달력   날짜    기준 하루 주기 ex) 하루주기: freq = 'D',이틀주기: freq = '2D'
#  B       업무   날짜    기준 하루 주기 ex) 업무일(월~금)기준으로 생성

# 2일씩 증가하는 날짜를 생성
print(pd.date_range(start='2024-01-01',periods=4,freq = '2D'))

# 달력의 요일을 기준으로 일주일씩 증가하는 날짜를 생성
print(pd.date_range(start='2024-01-01',periods=12,freq = 'B'))

# 분기 시작일을 기준으로 4개의 날짜를 생성
print(pd.date_range(start='2024-01-01',periods=4,freq = 'QS'))

# 연도의 첫날을 기준으로 1년 주기의 3개의 날짜 생성
print(pd.date_range(start='2024-01-01',periods=3,freq = 'AS'))

# 2) 시간 생성

# 1시간 주기로 10개의 시간을 생성
print(pd.date_range(start='2024-01-01 08:00',periods=10,freq = 'H'))

# 30분 단위로 4개의 시간을 생성
# 30min으로 설정해도 출력은 30T
print(pd.date_range(start='2024-01-01 08:00',periods=4,freq='30min'))

# 10초 단위로 5개의 시간을 생성
print(pd.date_range(start='2024-01-01 10:00',periods=5,freq='10S'))

# 문제: date_range()함수를 사용하여 2024년 1월 1일부터 2024년 12월 31일까지의 인덱스를 갖는 데이터 프레임을 생성하시오.
print(pd.date_range(start='2024-01-01',end='2024-12-31'))

