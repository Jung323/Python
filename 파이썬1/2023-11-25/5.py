# 변수 variable : 어떤 데이터를 저장하고자 할떄 사용하는 메모리 저장소


# 변수명 생성규칙
# 1. 영문, 한글, 숫자, 언더바(_) 로 구성
# 2. 특수문자는 사용이 안된다.
# 3. 대소문자는 구분이 된다. 예) Number 와 number 는 다른 변수로 취급된다.
# 4. 변수명의 첫 글자는 숫자를 사용할 수 없다. 예)my2002(O) / 2002my(X)
# 5. 키워드(list, dict, if, for, and 등)은 사용할 수 없다.

# 권장하는 변수명
# 1. 가급적 영문 소문자를 사용한다.
# 2. 한글을 사용하지 않고 영어 변수명을 사용한다.
# 3. 저장된 데이터가 변수명으로 유추가 가능하도록 사용한다. 예)number(숫자형 데이터),str(문자형 데이터)

name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호''' #multiple line 문자열 저장 →줄바꿈을 하더라도 '''안 내용은 하나의 문자열로 인식함
boyfriend = None #아무것도 저장하지 않음 / 다른언어에서는 null로 사용함 / python에서는 None이라고 표현
height = '170.5' #이렇게 저장해도 상황에 따라 문자열이 아니라 실수로 저장하기도 함

print(name)
print(age)
print(address)
print(boyfriend)
print(height)


print('-'*50)

print('내 이름은 ' + name)
print('내 나이는 ' + str(age))
print('남자친구의 유무: '+ str(boyfriend))
print('내 키는 ' + height)