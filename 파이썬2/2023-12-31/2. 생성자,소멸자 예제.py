# 생성자와 소멸자를 이용해서 서비스 안내 메시지를 출력하는 프로그램

class Service:
    def __init__(self,service):
        self.service = service
        print(f'{self.service}가 시작되었습니다.')

    def __del__(self):
        print(f'{self.service}가 종료되었습니다.')

s = Service('길 안내')