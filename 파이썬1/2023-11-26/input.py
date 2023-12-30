# 표준입력
# input() 함수 : 표준 입력 장치(키보드)로부터 입력받을 때 사용
# n =input('')
# print(n)

print()

n= input('정수를 입력하세요.')
print(n)
print(type(n)) #결과: <class 'str'>

n = int(input('정수를 입력하세요')) # 정수로 형변환
print(n)
print(type(n)) #결과: <class 'int'>