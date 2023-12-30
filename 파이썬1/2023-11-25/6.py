# 정수 int

# int()함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환할 수 있다.
# 즉, 내림된 숫자를 표시함
print(int(1.9)) #결과 : 1

print(int(True)) #결과 : 1 /True는 1으로 변환,사실상 0이외의 숫자가 들어오면 True로 판단
print(int(False)) #결과 : 0 / False는 0으로 변환
print(int('100')) #결과 : 100 /문자형 100을 숫자로 변환
print(type(100)) #결과 : <class 'int'> /의미: int(정수)형이다.


#10진수를 2진수, 8진수, 16진수로 변환하는 방법
print()
n = 95
print(type(n)) #<class 'int'>

print(bin(n)) #결과 : 0b1011111/ 2진수로 변환
print(oct(n)) #결과 : 0o137 / 8진수로 변환
print(hex(n)) #결과 : 0x5f / 16진수로 변환