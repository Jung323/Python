# 2. 배열의 연산
import numpy as np

# 1) 기본연산
# 배열의 형태 shape(행,열)이 같다면 덧셈, 뺄셈, 곱셈, 나눗셈 연산을 할 수 있다.

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([1,2,3,4,5])

# 덧셈 : 각 배열의 같은 위치의 원소를 더한다.
print(arr1 + arr2)

# 뺄셈 : 각 배열의 같은 위치의 원소를 뺸다.
print(arr1 - arr2)

# 상수곱셈 : 배열의 각 원소에 상수를 곱한다.
print(arr1 * 2)

# 거듭제곱
print(arr2 ** 2)

# 나눗셈 : 각 배열의 같은 위치의 원소를 나눈다.
print(arr1 / arr2)

# 복합연산
print(arr1 / (arr2 **2))

# 배열은 비교 연산도 가능. 원소별로 조건과 일치하는지 확인 후 일치하면 True, 불일치하면 False

print(arr1 > 20)

# 2) 통계를 위한 연산
# Numpy에는 배열의 합, 평균, 표준 편차, 분산, 최솟값과 최댓값, 누적 합, 누적 곱 등 주로 통계에서 많이 이용하는 메소드가 포함되어 있다.

arr3 = np.arange(5)
print(arr3)

# 합
print(arr3.sum()) # 결과: 10

# 평균
print(arr3.mean()) # 결과: 2.0

# 표준 편차 : 데이터가 얼마나 평균값에서 퍼져 있는지를 나타내주는 통계
print(arr3.std()) # 결과: 1.4142135623730951

# 분산
print(arr3.var()) # 결과: 2.0

# 최솟값
print(arr3.min()) # 결과: 0

# 최댓값
print(arr3.max()) # 결과: 4

arr4 = np.arange(1,5)
print(arr4) # 결과: [1 2 3 4]

# 누적합
print(arr4.cumsum()) # 결과: [ 1  3  6 10]

# 누적곱
print(arr4.cumprod()) # 결과: [ 1  2  6 24]


# 행렬 연산
# Numpy는 배열의 단순 연산뿐 아니라 선형 다수를 위한 행렬(2차원배열) 연산도 지원
# Numpy에서 행렬은 2차원 배열로 표현

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# 덧셈
C = A + B
print(C)

# 뺄셈
D = A - B
print(D)

# 곱셈
E = A * B
print(E)

# 나눗셈
F = A / B
print(F)

# axis : 배열의 축을 나타내는 파라미터(매개변수)
# 2차원 이상의 다차원 배열에서 각 차원의 축마다 연산을 수행할 수 있도록 지원
# 예) axis = 0 : 행(row)방향 / axis = 1 : 열(column)방향

arr5 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

# 행방향(axis = 0)으로 합을 계산
sum_by_column = np.sum(arr5,axis=0)
print(sum_by_column) # 결과:[12 15 18]