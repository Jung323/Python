# 구구단 2단부터 9단까지 출력
# 각 단 앞에 제목, 마지막에 구분선을 넣어 볼 것


a = 2
b = 1

while a < 10 :
    while b < 10:
        print(f'{a} X {b} = {a*b}')
        b += 1
    print(f'{a}단이 끝났습니다.')
    print('-'*20)
    a += 1
    b = 1


dan = int(input('구구단을 외자! 원하는 단수를 입력하세요: '))
n = 1
while dan < 10:
    while n < 10 :
        print(f'{dan} X {n} ={dan*n}')
        n += 1
    dan = 10