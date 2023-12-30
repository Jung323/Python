# method(메소드)
# 메소드란 특정 객체 object를 가지고 잇는 함수 function을 의미
# 함수는 독립적으로 호출할 수 있지만,
# 메소드는 특정 객체 소속이어서, 메소드를 호출하려면 특정 객체를 통해서만 호출 가능하다.

# 1. 문자열 메소드
# 문자열 str을 처리하기 위해 많은 메소드를 제공

# 1) format()

# 2) count()
# 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드

s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린')) #결과: 4

# 인덱스를 지정해서 범위를 지정할 수 있다.
s = 'best of best'
print(s.count('best',10)) # count를 시작할 인덱스를 지정
print(s.count('best',-7)) # 마이너스 인덱스도 가능하다

# 3) find()
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# 찾고자 하는 문자열이 있으면 그 문자열이 처음으로 나온 위치, 즉 인덱스를 반환한다.

s = 'apple'
print(s.find('p')) # 결과: 1
print(s.find('z')) # 결과 -1 / 찾는 문자열이 없는 경우 -1을 반환

# 인덱스를 이용해서 검색할 범위도 지정 가능하다.
# 시작할 인덱스를 지정하지 않는 경우에는 문자열의 처음부터 찾고, 시작할 인덱스를 지정하는 경우 지정된 인덱스부터 찾음

s = 'best of best'
print(s.find('best'))
print(s.find('best',5))

# 4) index()
# find() 메소드와 같음. 사용방법도 동일. 차이점은 문자열이 없을 때 발생
# find() 메소드는 찾는 문자열이 없는 경우 -1을 반환, index() 메소드는 오류 발생

s = 'apple'
print(s.index('p')) # 결과: 1
print(s.index('z')) # 결과: 오류

# 5) 대소문자 변환 메소드
# upper : 모두 대문자로 변환한 결과를 반환
# lower :  모두 소문자로 변환한 결과를 반환
# capitalize :  첫 글자는 대문자로 변환하고, 나머지는 소문자로 변환

s = 'BEST of best'
print(s.upper()) #결과: BEST OF BEST
print(s.lower()) #결과: best of best
print(s.capitalize()) #결과: Best of best

# 6) join()
# 인수로 전달한 반복 가능 객체(문자열, 리스트 등)의 각 요소 사이에 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 반환

print('-'.join('python')) #결과: p-y-t-h-o-n
print('+'.join((['a','b','c','d','e']))) #결과: a+b+c+d+e


# 포함하는 문자없이 단순하게 리스트의 요소들을 연결하고자 한다면 빈 문자열 사용

print(''.join(['x','y','z'])) #결과: xyz
a = {'a':'apple','b':'banana'}
print(''.join(a)) #결과: ab/딕셔너리의 경우 key를 연결

# 7) split()
# 하나의 문자열을 여러 개의 문자열로 분리해서 저장한 리스트를 반환
s = 'Life is too short'
s2 = s.split() #split() 메소드에 아무 인수도 전달하지 않으면 공백문자를 기준으로 각 문자열이 분리됨
print(s2) #걀과: ['Life', 'is', 'too', 'short']

s = '010-1234-5678'
s2 = s.split('-') # 공백 대신 특정 문자열을 기준으로 분리하는 방법
print(s2) #결과:['010', '1234', '5678']


# 8) replace()
# 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환

s = 'Life is too short'
s2 = s.replace('short','long')
print(s2) #결과: Life is too long

# 특정 문자열을 제거하기 위한 용도로 사용
s = '010-1234-5678'
s2 = s.replace('-','')
print(s2) #결과: 01012345678

# 9) strip()
# 불필요한 문자열 제거 메소드
# 문자열 양끝에 있는 불필요한 문자열을 제거
# lstrip() : 왼쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# rstrip() : 오른쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# strip() : 양 끝에 있는 불필요한 문자열을 제거한 결과를 반환

s = '               apple'
print(len(s))

s2 = s.lstrip()
print(len(s2))
print(s2) #결과: apple

# 공백 문자 이외에 불필요한 문자열을 직접 지정하여 제거

s = '<head'
s = s.lstrip('<')
print(s) #결과: head