# 출력하고자 하는 구구단을 입력받아 구구단을 출력 (단, while문 사용 금지)

dan = int(input('출력할 구구단을 입력하세요: '))

for n in range(1,10,1):
    print(f'{dan} X {n} = {dan * n}')

print()

for n in [1,2,3,4,5,6,7,8,9]:
    print(f'{dan} X {n} = {dan * n}')