# 인수와 매개변수
# 함수로 전달되는 인수(argument)를 저장하는 변수를 매개변수(parameter)라고 한다.

# 1. 인수가 있는 함수

def introduce(name,age):
    print(f'내 이름은 {name}이고, 나이는 {age}살입니다.')

introduce('정서이',27)
introduce(age=25,name='james')


def show(*args):
    for item in args:
        print(item)

show('python')
show('happy','birthday')

# 2. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용
# 매개변수로 기본값을 설정할 수 있다.

def hello(message = '안녕하세요') :
    print(message)
hello() #결과: 안녕하세요
hello('만나서 반갑습니다.') #결과: 만나서 반갑습니다.

# 디폴트 매개변수가 있는 경우 뒤로 배치

def hello2(name,message='안녕하세요'):
    print(f'{name}님 {message}')

hello2('김철수') #결과: 김철수님 안녕하세요
hello2('김철수','반갑습니다') #결과: 김철수님 반갑습니다

def hello3(name = '이철수',message='안녕하세요'):
    print(f'{name}님 {message}')

hello3() #결과: 이철수님 안녕하세요
hello3('김철수') #결과: 김철수님 안녕하세요
hello3('김철수','반갑습니다') #결과: 김철수님 반갑습니다
