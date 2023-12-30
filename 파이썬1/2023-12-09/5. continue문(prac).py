fruits = ['사과','수박']
count = 3 # 입력 가능한 횟수

# 문제
# 만약 동일한 과일이 입력될 경우 '동일한 과일이 있습니다.'가 출력되고 count는 차감되지 않는다.
# 만약 다른 과일이 입력된 경우 count가 차감되고 입력한 과일이 리스트에 추가된다.
# 그리고 차감된 이후 '입력이 ~번 남았습니다.'라는 문구가 떠야 한다.
# count가 0이 되면 종료가 된다. 종료가 된 후에는 '5개 과일은 ~입니다'가 출력이 되어야 한다.

while count > 0 :
    fruit = input('어떤 과일을 저장할까요?: ')
    if fruit in fruits:
        print('동일한 과일이 있습니다.')
        # count = count
        continue

    else :
        count -= 1
        fruits.append(fruit)
        print(f'입력이 {count}번 남았습니다.')

if count == 0:
    print(f'5개의 과일은 {fruits}입니다.')
