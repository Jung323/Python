# 일반 변수
num1 = 10
num2 = 20
print(num1)
print(num2)
# 일반변수는 변수 = 10 는 10이라는 숫자가 변수 안에다 들어감


# 참조 변수
# 참조변수는 10이라는 숫자가 변수 안에다가 들어가는 것이 아니라 10이라는 메모리 주소를 할당받는다.

class Score:

    # -> 함수 리턴 값의 주석 역할을 한다.
    def __init__(self,no:int) -> None:
        self.no = no

    def __str__(self) -> str :
        return str(self.no)

no1 = Score(30)
no2 = Score(40)
print(no1)
print(no2)

print(id(no1))
print(id(no2))

no2.no = 30
# no1,no2는 참조변수라서 주소가 복사
print(no1) # 결과: 30
print(no2) # 결과: 30
print(id(no1))
print(id(no2))


# 일반 변수 : 일반 변수는 값을 직접 지정하고 해당 변수를 다른 변수에 할당할 때 값이 복사된다.
# 대표적으로 int형, 부동소수점(float), 문자열(string), 불린(boolean)
a = 5
b = a
a = 10

print(a)
print(b) # 결과: 5 / a를 변경해도 b는 영향을 받지 않음

# 참조 변수 : 데이터의 주소값을 저장한다. 여러 변수가 같은 데이터를 참조할 수 있다.
# 데이터의 크기가 가변적이며, 메모리에 데이터를 저장하고 그 데이터의 주소를 변수에 저장한다.
# 대표적으로 리스트(list),딕셔너리(dictionary),객체(object) 등

list1 = [1,2,3]
list2 = list1 # list2가 list1을 참조
list1.append(4) # list1에 원소 추가
print(list2) # 결과:[1, 2, 3, 4]