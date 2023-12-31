# 클래스를 선언
# init은 클래스의 생성자


class MyClass:
    # self : 특별한 예약어. 클래스의 인스턴스 메서드 안에서 사용된다.
    # 해당 메서드가 호출된 인스턴스를 가리킨다. 즉, self는 클래스 MyClass를 뜻한다.
    # 생성자(__init__) : 클래스가 만들어질 때 무조건적으로 실행되는 함수
    # self.value = MyClass의 값
    def __init__(self,value):
        self.value = value
        # 1. 변수 입력하면 self.value 에 그 변수가 담긴다.

    def print_value(self):
        print(self.value)
        # 2. 변수가 담긴 self.value값을 프린트함

obj = MyClass(42)
obj.print_value()


class Student:
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f'{self.name}\t{self.get_sum()}\t\t{self.get_average()}'



students = [
    Student('연하진', 92, 98, 96, 98),
    Student('구지연', 76, 96, 94, 90),
    Student('나선주', 98, 92, 96, 92),
    Student('윤아린', 95, 98, 98, 98),
    Student('윤명월', 64, 88, 92, 92)
]

print('이름','총점','평균',sep='\t\t')
for student in students :
    print(student.to_string())
