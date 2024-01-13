# 1. 0부터 9까지의 정수로 이루어진 크기가 10인 1차원 배열을 생성하시오
# np.array금지
import numpy as np

arr1 = np.arange(0,10)
arr2 = np.linspace(0,9,10).astype(int)

print(arr1)
print(arr2)

# 2. 뽑은 1차원 배열의 순서를 반대로 바꿔보세요.
arr3 = np.arange(9,-1,-1)
print(arr3)

# 3. 주어진 두 배열의 덧셈,뺄셈,곱셈,나눗셈을 계산해보시오
arr4 = np.array([1,2,3,4,5])
arr5 = np.array([6,7,8,9,10])
print(arr4 + arr5)
print(arr4 - arr5)
print(arr4 * arr5)
print(arr4 / arr5)

# 4-1. 주어진 1차원 배열의 모든 요소의 합을 계산해보시오
arr6 = np.array([1,2,3,4,5])
print(arr6.sum())

# 4-2. 주어진 1차원 배열의 평균을 계산하시오
arr7 = np.array([10,20,30,40,50])
print(arr7.mean())

# 4-3. 주어진 1차원 배열에서 최댓값과 최솟값을 찾아보시오.
arr8 = np.array([17,12,25,9,30])
print(arr8.max())
print(arr8.min())