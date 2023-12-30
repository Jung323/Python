# 로또 추첨 프로그램은 당첨번호가 총 6개가 나온다. (1~45의 숫자 중 6개)

# 방법1

import random
lotto = random.sample(range(1,46),6)
for i in range(0,6):
    print(f'{i+1}번째 당첨번호는 {lotto[i]}입니다.')
lotto.sort()
print(f'이번 당첨번호는 {lotto}입니다.')

# 방법2
import time
import random

jackpot = []
while len(jackpot) <6:
    num = random.randint(1,45)

    if num not in jackpot:
        jackpot.append(num)
        print(f'{len(jackpot)}번째 당첨번호는 {num}입니다.')
        time.sleep(2)

# 당첨번호를 정렬하여 출력
jackpot.sort()
print(f'이번 당첨번호는 {jackpot}입니다.')