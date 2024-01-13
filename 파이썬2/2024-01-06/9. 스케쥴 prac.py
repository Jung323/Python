# 오늘의 스케쥴을 입력하면 그 내용이 모두 파일에 보관되는 프로그램이다.
# 스케쥴을 입력하지 않고 enter를 누르면 프로그램은 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-01-06.txt'와 같은 형식을 갖추고 있습니다.
# hint : time 모듈을 불러오시오. time.strftime을 사용하시오

import time

file = open(f'./output/{time.strftime('%Y-%m-%d')}.txt','wt',encoding='utf-8')
while True:
    s = input('오늘의 스케쥴을 입력하세요: ')
    if s == '':
        exit()
    else:
        file.write(s +'\n')
