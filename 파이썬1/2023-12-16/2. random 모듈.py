# 2. random 모듈
# 난수(random number)를 생성하는 모듈
# 난수를 통해서 간단한 게임을 제작할 수 있고 확률 처리도 할 수 있다.

import random
# 1) randint() 함수
# 전달하는 두 인수 사이의 정수를 임의로 생성

print(random.randint(1,10)) # 1이상 10이하의 정수

# 2) randrange() 함수
# range() 함수와 사용방법이 비슷
# range() 함수는 특정 범위의 정수값을 모두 생성할 수 있지만
# randrange() 함수는 그 특정 범위에 속한 정수중 하나만 임의로 생성

print(random.randrange(10)) # 0이상 10 미만의 정수
print(random.randrange(1,10)) # 1이상 10 미만의 정수
print(random.randrange(1,10,2)) # 1이상 10미만의 홀수

# 3) random() 함수
# 0이상 1미만 범위에서 임의로 실수를 생성
# 0이상 1미만 번위를 백문율로 환산하면 0%이상 100%미만이기 때문에 확률을 처리할 때도 사용
print(random.random())

# 50% 확률로 '안녕하세요'출력
if random.random() <= 0.5:
    print('안녕하세요')

rand = random.randint(1,2)
print(rand)
if rand == 1:
    print('안녕하세요')

# 4) choice() 함수
# 전달된 시퀀스 자료형에 속한 요소 중에서 하나를 임의로 반환
seasons = ['spring','summer','fall','winter']
print(random.choice(seasons))

idx = random.randint(0,3)
print(seasons[idx])

# 5) sample() 함수
# 전달된 시퀀스 자료형에 속한 요소중 지정된 개수의 요소를 임의로 반환
# 반환 결과는 리스트(list)자료형이며 중복없이 임의의 요소가 선택

print(random.sample(range(1,101),10)) #1이상 101미만의 숫자중에서 10개의 정수가 리스트로 나옴

# 6) shuffle() 함수
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list) # 리스트의 순서가 마음대로 섞임

