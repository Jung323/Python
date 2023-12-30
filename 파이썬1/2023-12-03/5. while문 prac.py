# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력하는 프로그램을 구현하세요.
# 0 이하의 값이 입력되면 '잘못된 입력입니다.' 라는 오류 메시지를 출력하세요.

#방법1

n = int(input('정수를 입력하세요: '))
a = 1
if n > 0:

    while a <= n :
        print(f'{a}번째 Hello')
        a += 1
else:
    print('잘못된 입력입니다.')

print()

#방법2

# n = int(input('정수를 입력하세요: '))
# b = 1
# if n <= 0 :
#     print('잘못된 입력입니다.')
#     exit()
# while b <= n:
#     print(f'{b}번째 Hello')
#     b += 1







# 1부터 100사이의 모든 정수 중에서 7의 배수만 출력하는 프로그램을 구현하세요.

#방법1

n = 1
while n <= 100 :
    if n % 7 == 0 :
        print(n)
    n += 1

print()

#방법2

# n = 7
# while n <= 100:
#     print(n)
#     n += 7

