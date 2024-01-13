# 예외 처리
# 1. 고전적인 예외 처리
# 개발자가 직접 처리

a = int(input('제수를 입력하세요 : '))
b = int(input('피제수를 입력하세요 : '))

if b == 0:
    print('0으로 나누는 것은 불가능합니다.')
else :
    print(f'{a}/{b} = {a/b}')

# 고적적인 예외 처리 방식의 문제점
# 1) 어떤 문제가 발생했는지 예상할 수 있어야 대비가 가능
# 2) 어떤 문제가 발생할지 예상을 하더라도 대비할 수 없는 경우가 있다.

# 2. except를 이용한 예외처리
try:
    a = int(input('제수를 입력하세요 : '))
    b = int(input('피제수를 입력하세요 : '))
    print(f'{a}/{b} = {a/b}')

except:
    print('예외가 발생했습니다.')

# except는 모든 예외를 처리를 해주어 사용자가 어떤 오류인지 분별하기 어렵다.


# 3. 의도적 예외
# 특정한 에외를 지정함
try:
    a = int(input('제수를 입력하세요 : '))
    b = int(input('피제수를 입력하세요 : '))
    print(f'{a}/{b} = {a/b}')

except ZeroDivisionError :
    print('0으로 나눌 수 없습니다.')
except ValueError :
    print('정수만 입력받을 수 있습니다.')


# 4. 예외 메시지 처리하기
# 지금까지 모든 예외 메시지를 직접 만들어서 사용
# 하지만 모든 예외는 기본 예외 메시지를 가지고 있다.
# 예외들이 가지고 있는 예외 메시지를 확인하려면 except문에 as절을 추가해서 예외 메시지를 받아 사용함.

# try:
#   코드 작성 영역
# except 예외 as 예외 메시지:
#   예외 발생 시 처리 영역

a = [10,20,30,40,50]
try:
    a[10]
except IndexError as e:
    print(e) #결과: list index out of range
