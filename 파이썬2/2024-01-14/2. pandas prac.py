# 1. 주어진 데이터 프레임 df에는 Name(이름),Age(나이),Salary(월급) 열이 있다.
# 주어진 데이터 프레임은 다음과 같다.
import pandas as pd

data = {'Name':['Amy','Bob','Chad','Dave','Emma'],
        'Age':[25,30,35,40,45],
        'Salary':[3000,4000,5000,6000,7000]}
df = pd.DataFrame(data)
print(df)

# 1. Salary열의 평균값을 계산하시오
print(df['Salary'].mean())

# 2. Age열의 최댓값을 계산하시오
print(df['Age'].max())

# 3. Name열에서 a를 포함한 이름만 선택하여 출력하시오
# hint : str.contains()함수를 이용하세요
print(df[df['Name'].str.contains('a')])