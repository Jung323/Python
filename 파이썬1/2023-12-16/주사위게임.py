# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 맞히는 프로그램입니다.
# 사용자가 맞힐 때까지 게임은 계속됩니다.

import random
answer = random.randint(1,6)

while True:
    number = int(input('주사위 값은 얼마일까요?: '))
    if number == answer:
        print(f'{answer}! 정답입니다.')
        break
    elif number > answer:
        print('오답입니다. 다시 시도하세요.')
        print('다운')
    else:
        print('오답입니다. 다시 시도하세요.')
        print('업')
