
# 비시퀀스 자료형을 이용한 반복

# 1. 세트 set
# 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음

# 기본 형식
# for 요소 in {세트}
#   반복실행문

for item in {'가위','바위','보'} :
    print(item)

print()
# 2. 딕셔너리
# key 와 value의 조합이라 다른 자료형과 다른 방식으로 사용해야 한다.

# key만 출력
person = {'name':'emily','age' : 20}
for item in person:
    print(item)

print()

# value만 출력
for key in person :
    print(f'{person[key]}')

print()

for key in person: # get() 메소드를 이용해서 해당 key에 해당하는 value를 가져온다.
    print(f'{person.get(key)}')

print()

# key,value 모두 출력
# 이 형식을 사용하는 걸 추천함
for key, value in person.items():
    print(f'{key}:{value}')

