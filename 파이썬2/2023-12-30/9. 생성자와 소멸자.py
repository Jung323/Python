# 생성자와 소멸자

# 1. 생성자
class Candy:
    def set_info(self,shape,color):
        self.shape = shape
        self.color = color

    def print_info(self):
        print(f'모양 : {self.shape}, 색깔 : {self.color}')

satang = Candy()
satang.set_info('circle','green')
satang.print_info()

# satang = Candy() 코드가 실행되면서 satang 인스턴스(객체)가 생성되는데
# 이떄는 인스턴스에 저장된 모양과 색상정보가 없음
# 인스턴스 생성 후에 set_info() 메소드를 호출해서 색상 정보를 가진다.
# 정리하자면
# 1) 값이 없는 인스턴스 생성
# 2) 값을 저장할 수 있는 메소드를 호출

# 값을 가진 인스턴스를 생성하기 위해 생성자를 이용
# 생성자느 인스턴스를 생성할 때 자동으로 호출되는 특별한 메소드
# 모든 클래스는 __init()라는 이름을 가진 생성자를 가지고 있다.
# __init__() 메소드(생성자)는 인스턴스가 생성될 떄 자동으로 호출되기 때문에 인스턴스 변수의 초기화 용도로 사용

# __init__
# 새로운 인스턴스가 만들어질 떄 자동으로 호출되는 메소드
# 생성자는 아님. 생성자는 '__new__'이고, 생성자가 객체를 메모리에 할당해서 리턴을 하는데
# 리턴을 하기 전에 __init__메소드를 호출
# __init__에서는 '새로운 속성을 추가하는 일'을 해야한다.

class Candy():
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color

satang = Candy('circle','brown')

# 2. 소멸자
# 인스턴스가 소멸될 떄 자동으로 호출되는 메소드
# 소멸자는 __del__()

class Sample:
    def __init__(self):
        print('인스턴스가 생성됩니다.')
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample()

del sample # 소멸자를 즉시 명령