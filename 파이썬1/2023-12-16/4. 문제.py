# 1) 나이를 입력받아 19세 이상이면 1250원,13~18세이면 1050원,7~12세이면 650원,7세 미만은 0원을 지불하고 잔액은 ...입니다를 출력하시오.
money = 9000

age = int(input('나이를 입력하세요: '))
if age >= 19:
    charge = 1250
elif age >= 13 and age <= 18:
    charge = 1050
elif age >= 7 and age<= 12:
    charge = 650
else:
    charge = 0
print(f'나이가 {age}인 승객의 요금은 {charge}원이고 잔액은 {money-charge}원입니다.')

print()

# 2) 사용자로부터 하나의 정수를 입력받고 정수가 홀수인지 짝수인지 판별하여 출력

n1 = int(input('하나의 정수를 입력하세요: '))
if n1 % 2 == 0 :
    print('입력한 숫자는 짝수입니다.')
else:
    print('입력한 숫자는 홀수입니다.')

print()

# 3) 사용자로부터 정수를 입력받아 해당 정수의 구구단을 출력하는 프로그램을 작성하시오
dan = int(input('몇 단을 할까요? : '))
for i in range(1,10):
    print(f'{dan} X {i} = {dan*i}')

print()

# 4) 사용자로부터 여러 개의 숫자를 입력받아 입력된 숫자 중에서 가장 큰 값을 찾아 출력하는 프로그램을 작성하시오.
#   숫자입력은 무한대로 받을 수 있다. 단, -1을 입력하는 순간 종료

num_list = []

while True:
    n2 = int(input('숫자를 입력하세요: '))
    if n2 == -1:
        print(f'입력한 숫자 중에서 가장 큰 수는 {max(num_list)}입니다.')
        break
    else:
        num_list.append(n2)



print()

# 4) 사용자로부터 하나의 정수를 입력받아 해당 숫자만큼 높이를 가진 삼각형 모양의 별을 출력하는 프로그램을 작성하시오.

n3 = int(input('하나의 정수를 입력하세요: '))
for i in range(1,n3+1):
    print('*'*i)
