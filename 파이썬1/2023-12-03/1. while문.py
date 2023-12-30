# while 문
# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할때 사용

#while 조건식 :
#   반복실행문

n = 1
while n <= 10:
    print(n)
    n += 1 # n = n + 1
print(n)

# while문의 중첩
# while문 내부에 또 다른 while문이 나타나는 것

day = 1
while day <= 5:
    hour = 1
    while hour <= 3:
        print(f'{day}일차 {hour}교시 입니다.')
        hour += 1
    day += 1