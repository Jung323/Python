# Numpy : 배열 데이터를 효과적으로 다룰 수 있다.
# 2016년부터 파이썬이 본격적으로 핵심언어가 되기 시작
# Numpy를 이용하면 파이썬의 기본 데이터 형식과 내장 함수를 이용하는 것보다 다차원 배열 데이터를 효과적으로 처리할 수 있다.
# Numpy 홈페이지 : https://numpy.org/

# 1. 배열 생성
# Numpy는 파이썬의 내장모듈이 아니라서 별도로 설치해야 사용가능

import numpy as np
# 배열(Array)이란 순서가 있는 같은 종류의 데이터가 저장된 집합
# Numpy를 이용해 배열을 처리하기 위해서는 우선 Numpy로 배열을 생성해야 한다.
# 다양한 방법으로 배열을 생성하는 방법 보기

# 1) 시퀀스 데이터로부터 배열 생성하기. array()
# 시퀀스 데이터 seq_data를 인자로 받아 Numpy의 배열 객체(array object)를 생성
# arr_obj = np.array(seq_data)

# 정수 리스트로 배열 생성
data1 = [0,1,2,3,4,5]
print(data1) # 결과: [0, 1, 2, 3, 4, 5] / 콤마(,)가 들어가 있으면 리스트

a1 = np.array(data1)
print(a1) # 결과: [0 1 2 3 4 5] / 콤마(,)가 없으면 numpy
print(a1.dtype) # 결과: int32

# 정수와 실수가 혼합된 경우
data2 = [0.1,5,4,12,0.5]
a2 = np.array(data2)
print(a2) # 결과: [ 0.1  5.   4.  12.   0.5]
print(a2.dtype) # 결과: float64 / 정수와 실수가 혼합되어있을 경우 모두 실수로 변환

# 배열의 속성을 표현할 때는 'np.array.속성'과 같이 작성
a3 = np.array([0.5,2,0.01,8])
print(a3) # 결과: [0.5  2.   0.01 8.  ]

# 다차원 배열의 생성
# 2차원 배열: 가로,세로 / 3차원: 가로,세로,높이
a4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a4)

# 2) 범위를 지정해 배열 생성하기. arange()
# arange()를 이용해 Numpy 배열을 생성. 파이썬의 range()와 사용방법이 비슷
# arr_obj = np.arange([start,stop,step])
# start부터 시작해서 stop 전까지 step 만큼의 간격으로 Numpy 배열을 생성
# start가 0인 경우, step이 1인 경우 생략가능

a1 = np.arange(0,10,2)
print(a1) # 결과: [0 2 4 6 8]

a2 = np.arange(1,10)
print(a2) # 결과: [1 2 3 4 5 6 7 8 9]

a3 = np.arange(5)
print(a3) # 결과: [0 1 2 3 4]

# Numpy 배열의 arange()를 이용해 생성한 1차원 배열에 reshape(m,n)을 추가하면 m*n 형태의 2차원 배열(행렬)로 변경
# 주의할 점: arange()로 생성되는 배열의 원소개수와 reshape(m,n)의 m*n의 개수가 같아야 한다.

a4 = np.arange(12).reshape(4,3) # reshape(행수,열수)
print(a4)

# 결과:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Numpy배열의 형태를 알기 위해서는 '.shape'를 실행
print(a4.shape) # 결과: (4, 3)

# 1차원 배열의 경우 '(n,)'처럼 표시
print(a1.shape) # 결과: (5,)



# .linspace()
# 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 배열을 생성
# arr_obj = np.linspace(start,stop,num)
# linspace()는 start부터 stop까지 num개의 배열을 같은 간격으로 생성, num을 지정하지 않으면 50이 기본값

a1 = np.linspace(1.,10,10)
print(a1) # 결과: [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

a2 = np.linspace(1.,10,4)
print(a2) # 결과: [ 1.  4.  7. 10.]

a3 = np.linspace(0,np.pi,5) # numpy만의 pi를 이용해 동일한 간격으로 5개로 나눈 배열 생성
print(a3)  # 결과: [0.         0.78539816 1.57079633 2.35619449 3.14159265]

# 3) 배열의 데이터 타입 변환하기
# 배열은 숫자뿐만 아니라 문자열도 원소를 가질 수 있다.
a1 = np.array(['1.5','0.62','2','3.14'])
print(a1) # 결과: ['1.5' '0.62' '2' '3.14']
print(a1.dtype) # 결과: <U4 , 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 것을 의미

# Numpy 데이터의 형식
# b: 참/거짓, bool(boolean)
# i : 기호가 있는 정수,(signed) integer
# u : 기호가 없는 정수, unsigned integer
# f : 실수, floating-point(float)
# c : 복소수, complex-floating point
# M : 날짜, datetime
# O : 파이썬 객체, (python) objects
# U : 유니코드, Unicode / 유니코드 전에는 아스키 코드가 존재

# 배열이 문자열(숫자 표시)로 되어 있다면 연산을 위해서는 문자열을 숫자(정수나 실수)로 변환해야 한다.
# 데이터 형식의 변환은 astype()로 가능
# num_arr = str_arr.astype(dtype)


# 실수가 입력된 문자열을 원소로 갖는 배열을 실수타입으로 변환하는 예

str_a1 = np.array(['1.567','0.123','5.123','9','6'])
num_a1 = str_a1.astype(float) # 실수타입으로 변환
print(str_a1) # 결과: ['1.567' '0.123' '5.123' '9' '6']
print(num_a1) # 결과: [1.567 0.123 5.123 9.    6.   ]
print(str_a1.dtype) # 결과: <U5
print(num_a1.dtype) # 결과: float64

# 정수를 문자열 원소로 갖는 배열을 정수로 변환하는 예

str_a2 = np.array(['1','3','5','7','9'])
num_a2 = str_a2.astype(int)
print(num_a2) # 결과: [1 3 5 7 9]
print(str_a2.dtype) # 결과: <U1
print(num_a2.dtype) # 결과: int32

# 실수를 원소로 갖는 배열을 정수로 변환하는 예

num_f1 = np.array([10,21,0.549,4.75,5.98])
num_i1 = num_f1.astype(int)
print(num_i1) # 결과: [10 21  0  4  5] / 정수로 변환할 때는 내림처리
print(num_f1.dtype) # 결과: float64
print(num_i1.dtype) # 결과: int32