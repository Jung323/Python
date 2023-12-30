# and 연산자
# 결과값은 True와 False 둘 중 하나
# a and b : a 와 b가 모두 참(True)이면 True, 둘 중 하나라도 거짓(false)이면 False

# or 연산자
# a or b : a 와 b중 하나라도 참(True)이면 True, 둘 다 거짓(false)이면 False

# not 연산자(!)
# 0 이 False이다. 다른 숫자들은 모두 참(True)이다.
# True면 False, False이면 True가 된다.
# 쉽게 생각하면 0인지 묻는 것 → 0이면 참, 0이 아니면 거짓

a = 10
b = 0

print(f'{a} > 0 and {b} > 0 : {a > 0 and b > 0}') #결과: 10 > 0 and 0 > 0 : False
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}') #결과: 10 > 0 or 0 > 0 : True
print(f'not {a} : {a, not a}') #결과: not 10 : (10, False)
print(f'not {b} : {b, not b}') #결과: not 0 : (0, True)