# 커피 자판기 프로그램
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# '아메리카노' : 1000
# '카페라떼' : 1500
# '카푸치노' : 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환



def coffee_machine(menu,money):
    menu_list = {'아메리카노': 1000, '카페라떼': 1500, '카푸치노': 2000}
    if menu in menu_list :
        price = menu_list[menu]
        if money >= price:
            change = money - price
            print(f'{menu}를 선택하셨으며, 넣으신 돈은 {money}원입니다.')
            return menu,change
        else :
            change = money
            print(f'금액이 부족합니다.')
            return menu, change
    else :
        change = money
        print(f'메뉴가 존재하지 않습니다.')
        return '없는 메뉴',change

mypick = input('주문할 메뉴를 입력하세요: ')
mymoney = int(input('지불할 돈을 입력하세요: '))

pick, mychange = coffee_machine(mypick,mymoney)
print(f'주문한 커피는 {pick}입니다. 잔돈은 {mychange}원입니다.')



# 강사님 코드
def coffee_machine(money,pick):
    print(f'{money}원에 {pick}을 선택하셨습니다.')
    menu = {'아메리카노': 1000, '카페라떼': 1500, '카푸치노': 2000}

    if pick not in menu:
        print(f'{pick}은 판매하지 않습니다.')
        return money,'없는 메뉴'
    elif menu[pick] > money : # 구메할 금액이 부족할 겨우
        print(f'{pick}은 {menu[pick]}원입니다.')
        return money,'금액부족'
    else: #정상주문이면 잔돈과 선택한 커피를 반환
        return money - menu[pick],pick

order = input('커피를 선택하세요(아메리카노,카페라떼,카푸치노): ')
pay = int(input('얼마를 낼까요?: '))

change, coffee = coffee_machine(pay,order)
print(f'잔돈: {change}원, 커피: {coffee}')

