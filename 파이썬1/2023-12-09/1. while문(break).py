# break문
# while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# 반복문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문은 종료

n = 1
while n <= 10 :
    print(n)
    n += 1

print(n) # 이때의 n은 11

print()

n = 1
while True:
    print(n)
    if n == 10:
        break # if문에서 break문을 작성했지만 실제로 종료되는 것은 while문
    n += 1

print(n) # 이때의 n은 10, 10에서 이미 종료되어서 +1이 되지 않음.
