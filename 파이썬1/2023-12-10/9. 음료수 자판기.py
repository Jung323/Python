# 700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요
# 함수정의
# *반환값 : 없음
# 함수이름 : vending_machine()
# 매개변수 : 정수 money

# 코드 구성

def vending_machine(money):
    count = money // 700
    for i in range(0,count+1):
        change = money - i*700
        print(f'음료수 = {i}개, 잔돈 = {change}원')

vending_machine(3000)
