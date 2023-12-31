# 클래스 메소드와 정적 메소드
# 1. 클래스 변수
# 클래스를 구현할 때 인스턴스마다 서로 다른 값을 가지는 경우에는 인스턴스 변수를 사용
# 모든 인스턴스 변수들은 self 키워드를 붙여서 사용
# 모든 인스턴스가 동일한 값을 사용할 때는 클래스 변수로 처리해서 모든 인스턴스들이 공유하도록 처리하는 것이 좋음
# 인스턴스 변수는 인스턴스마다 값을 별도로 저장해야 하지만
# 클래스 변수는 하나의 값을 모든 인스턴스가 공유하기 때문에 메모리 공간의 낭비를 막을 수 있음

# self
# 관례적으로 모든 메소드의 첫번째 매개변수 이름을 self로 지정
# self가 파이썬의 예약어는 아니다.
# 파이썬의 객체와 관련된 설계에 영향을 준 스몰톡(smalltalk)이라는 프로그램에서 왔음

class Korean:
    country = '한국' # 클래스변수 country

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address =address

print(Korean.country) #결과: 한국\

man = Korean('홍길동',35,'대구')
print(man.name,man.age,man.address,man.country)

# 객체 프로퍼티 생성(동일한 이름의 클래스 변수)
# 객체의 변수 생성,클래스 변수가 아닌 인스턴스 변수를 바꿈
man.country = '미국' # 즉, man객체의 country라는 인스턴스 변수와 country라는 클래스 변수 2개가 존재함.
print(man.country) #결과: 미국
print(man.__class__.country) #결과: 한국

# 객체의 프로퍼티 생성
man.company = '현대'
print(man.company)

#클래스 변수 값 변경
# 1)객체를 이용
man.__class__.country = '영국'
print(Korean.country) #결과: 영국

# 2)클래스를 이용
Korean.country = '미국'
print(Korean.country) #결과: 미국

man2 = Korean('김길동',38,'서울')
print(man2.country) #결과: 미국
print(Korean.country) #결과: 미국



class Student:
    school = '서울대학교'

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{Student.school} {self.grade}학년 {self.name}'


hong = Student('홍길동',3)
print(hong) #결과: 서울대학교 3학년 홍길동 / 원래는 주소값이 결과로 나오지만 내용이 나오게 됨

print(hong.school) #결과: 서울대학교
hong.school = '경북고등학교' # 클래스 변수가 아닌 hong이라는 인스턴스에 school이라는 속성이 생성된 것
print(hong.school) #결과: 경북고등학교
print(hong) #결과: 서울대학교 3학년 홍길동 / 클래스 변수는 바뀌지 않았음

# 2. 클래스 메소드
# 클래스 변수를 사용하는 메소드를 의미
# 주요 특징
# 1) 인스턴스 혹은 클래스로 호출
# 2) 생성된 인스턴스가 없어도 호출할 수 잇음
# 3_ @classmethod 데코레이터(decorator)를 표시하고 작성
# 4) 매개변수 self를 사용하지않고 cls를 사용
# 클래스 메소드 self를 사용하지 않기 때문에 인스턴스 변수에 접근할 수 없지만,
# cls를 통해 클래스 변수에 접근할 수 있음

class Korean:
    country = '한국'

    @classmethod
    def trip(cls,country):
        if cls.country == country:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korean.trip('한국')
Korean.trip('미국')


# 3. 정적 메소드
# 1) 인스턴스 또는 클래스로 호출
# 2) 생성된 인스턴스가 없어도 호출 가능
# 3) @staticmethod 데코레이터(decorator)를 표시하고 작성
# 4) 반드시 작성해야 할 매개변수가 없음.

# 정적 메소드는 self와 cls를 모두 사용하지 않기 때문에 인스턴스 변수와 클래스 변수를 사용하지 않는 메소드를 정의하는 경우에 적절

#정적 메소드는 클래스에 소속되어 있지만, 인스턴스에 영향을 주지도 받지도 않음

class Korean:
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagine your korean')

Korean.slogan()