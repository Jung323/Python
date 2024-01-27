import numpy as np

# 1. 주어진 2차원 배열에서 가장 큰 값과 가장 작은 값을 찾는 Numpy코드를 작성하시오
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.max())
print(arr1.min())

# 2. 주어진 1차원 배열의 요소들을 오름차순으로 정렬하는 Numpy코드를 작성하시오
arr2 = np.array([4,9,2,3,8])
print(np.sort(arr2))

# 3. 주어진 2차원 배열의 각 행에 대해 합계를 계산하는 Numpy코드를 작성하시오
sum_by_column = np.sum(arr1,axis = 0)
print(sum_by_column)

# 4. 주어진 2차원 배열의 각 열에 대해 합계를 계산하는 Numpy코드를 작성하시오.
sum_by_row = np.sum(arr1,axis = 1)
print(sum_by_row)

# 5. 주어진 1차원 배열의 요소 중에서 3보다 큰 값들만 선택하는 Numpy코드를 작성하시오.
print(arr2[arr2>3])