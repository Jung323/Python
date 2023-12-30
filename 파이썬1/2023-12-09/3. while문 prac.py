# 다음은 break문을 사용하여 사용자로부터 숫자를 입력받고 입력된 숫자가 10보다 크면 반복문이 종료되고
# 10보다 작으면 계속 반복되는 코드를 만들어 보시오.

while True:
    number = float(input('숫자를 입력하세요: '))
    if number > 10 :
        print('입력한 숫자가 10보다 큽니다.')
        break
    elif number == 10 :
        print('입력한 숫자는 10과 같습니다.')
    else :
        print('입력한 숫자가 10보다 작습니다.')

