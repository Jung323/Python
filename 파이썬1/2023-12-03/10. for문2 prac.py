# 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 1부터 입력받은 정수까지 모든 정수의 합계를 출력하는 프로그램을 구현하세요.

num = int(input('임의의 정수를 입력하세요: '))
total = 0
for n in range(1,num+1):
    total += n
print(f'1부터 {num}까지의 모든 정수의 합계는 {total}입니다.')


# 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일이름'을 입력받아 'basket'리스트에 저장하는 프로그램을 구현하세요.

a = int(input('몇 개의 과일을 보관할까요?: '))
basket = []

for i in range(1,a+1):
    fruit = input(f'{i}번째 과일을 입력하세요: ')
    basket.append(fruit)
print(basket)
