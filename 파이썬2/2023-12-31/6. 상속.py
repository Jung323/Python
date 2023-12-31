# 상속
# 1. 상속이란?
# 어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 만들 수 있다.
# 다른 클래스의 기능을 물려받을 때 상속받는다 라는 표현을 사용
# 그래서 상속 관계에 있는 클래스를 표현할 때 부모 콜래스와 자식 클래스 라는 말을 사용

# 부모 클래스 : 상속 해주는 클래스 / 슈퍼 클래스(super class), 기반 클래스(base class)
# 자식 클래스 : 상속 받는 클래스 / 서브 클래스(sub class), 파생 클래스(derived class)

# 2. 상속 관계 구현
# 기본적으로 두 클래스가 상속 관계에 놓이려면 IS-A 관계가 성립되어야 한다.
# IS-A 관계란 '~은 ~이다'로 해설할 수 있는 관계를 의미
# 예를 들어 Student is a person 이 IS-A관계
# 이 때 Student는 서브 클래스가 되고, Person은 슈퍼 클래스가 됨


# 객체 지향 프로그래밍을 처음 접하면 두 클래스가 어떤 관계를 갖고 있을 때
# IS-A관계일 때는 상속으로 구현
# HAS-A관계일 때는 상속이 아닌 구성(composition)으로 구현


# class 슈퍼 클래스:
#   본문

# class 서브 클래스(슈퍼 클래스):
#   본문

# 서브 클래스를 구현할 때는 괄호 안에 어떤 슈퍼 클래스를 상속받는지 명시
# 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용할 수 있다.


class Person: # 슈퍼 클래스
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print(self.name + '가 ' + food + '를 먹습니다.')


class Student(Person): # 서브 클래스
    def __init__(self,name,school):
        super().__init__(name) # 슈퍼 클래스의 생성자 실행
        self.school = school

    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')

potter = Student('해리포터','호그와트')
potter.eat('감자')
potter.study()


# 3. 서브 클래스의 __init()
# 서브 클래스의 생성자를 구현할 때는 반드시 슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야 함
# super라는 키워드는 슈퍼 클래스를 의미

class Computer: # 슈퍼 클래스
    def __init__(self):
        print('슈퍼 클래스의 생성자가 실행되었습니다.')

class Notebook(Computer):
    def __init__(self):
        super().__init__() # super라는 키워드를 무조건 사용하여 부모클래스를 불러와야함.
        print('서브 클래스의 생성자가 실행되었습니다.')

n = Notebook()


# 4. 서브 클래스의 인스턴스 자료형
# 슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스
# 서브 클래스 객체는 서브 클래스의 인스턴스인 동시에 슈퍼 클래스의 인스턴스

# 어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 isinstance()함수를 사용하기도 함.
# 객체가 인스턴스일 경우에는 True 아니면 False 반환

print(isinstance(potter, Student))
print(isinstance(potter, Person))