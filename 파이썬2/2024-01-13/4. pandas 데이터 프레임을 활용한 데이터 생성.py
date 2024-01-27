import pandas as pd

data = {'Name':['John','Mike','Sarah','Kate'],
        'Math':[90,80,95,75],
        'English':[85,90,92,88],
        'Science':[92,88,78,88]}

df = pd.DataFrame(data)
print(df)
# 결과:
#     Name  Math  English  Science
# 0   John    90       85       92
# 1   Mike    80       90       88
# 2  Sarah    95       92       78
# 3   Kate    75       88       88

# 각 학생의 총점을 계산하고 싶으면?
df['Total'] = df['Math']+df['English']+df['Science']
print(df)
# 결과:
#     Name  Math  English  Science  Total
# 0   John    90       85       92    267
# 1   Mike    80       90       88    258
# 2  Sarah    95       92       78    265
# 3   Kate    75       88       88    251

# DataFrame을 활용한 데이터 생성
# 표(Table)와 2차원 데이터 처리를 위해 DataFrame을 제공
# 데이터 Data를 담는 틀(Frame)이라는 뜻

# 1)DataFrame을 이용해 데이터를 생성하는 방법
# df = pd.DataFrame(date,[index = index_data,columns=columns_data])
# data인자에는 리스트와 형태가 유사한 타입은 모두 사용 가능
# 즉 리스트,딕셔너리 numpy의 배열 데이터, Series나 DataFrame타입의 데이터는 입력이 가능
# 세로축 라벨을 index라 하고, 가로축 라벨을 columns라고 한다.
# index와 columns를 제외한 부분으로 values라고 한다.

import pandas as pd

d1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(d1)

# values 부분에는 일정한 data가 순서대로 입력되어있고 가장 좌측의 열과 가장 윗줄의 행은 각각 숫자가 자동으로 index,columns를 구성

# 명시적으로 index와 columns를 입력하지 않더라도 자동으로 index,columns가 생성되는 구조이다.

# 2)numpy배열 데이터를 입력해 생성한 DataFrame데이터의 예

import numpy as np

data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
d2 = pd.DataFrame(data_list)
print(d2)

# data뿐만 아니라 index와 column도 지정한 예
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2024-01-01',periods=4)
columns_list = ['A','B','C']
d3 = pd.DataFrame(data,index=index_date,columns=columns_list)
print(d3)
# 결과:
#              A   B   C
# 2024-01-01   1   2   3
# 2024-01-02   4   5   6
# 2024-01-03   7   8   9
# 2024-01-04  10  11  12


# 3)딕셔너리 타입으로 2차원 데이터를 입력한 예
table_data = {'연도':[2015,2016,2016,2017,2017],
              '지사':['한국','한국','미국','한국','일본'],
              '고객수':[200,250,450,300,500]}
d4 = pd.DataFrame(table_data)
print(d4)
# 결과:
#      연도  지사  고객수
# 0  2015  한국  200
# 1  2016  한국  250
# 2  2016  미국  450
# 3  2017  한국  300
# 4  2017  일본  500

d5 = pd.DataFrame(table_data,columns=['지사','고객수','연도'])
print(d5)
# 결과:
#    지사  고객수    연도
# 0  한국  200  2015
# 1  한국  250  2016
# 2  미국  450  2016
# 3  한국  300  2017
# 4  일본  500  2017

# DataFrame 데이터에서 index, columns, values를 각각 구한 예
print(d5.index)
# 결과: RangeIndex(start=0, stop=5, step=1)
print(d5.columns)
# 결과:Index(['지사', '고객수', '연도'], dtype='object')
print(d5.values)
# 결과:
# [['한국' 200 2015]
#  ['한국' 250 2016]
#  ['미국' 450 2016]
#  ['한국' 300 2017]
#  ['일본' 500 2017]]