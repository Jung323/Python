# 1. 텍스트 파일 읽기

# 1) read() 메소드
# file.read(size)
# 파일로부터 데이터를 읽어오는 메소드
# 파일 내용 전체를 가져와 문자열로 반환
file = open('./input/hello.txt','rt') # rt는 txt형식을 read한다는 의미

str = file.read()
print(str)

file.close()

# read() 메소드를 통해 전체를 읽으려면 그만큼의 메모리 공간을 필요
# 읽어야 할 파일이 크다면 일부만 읽어 들이는 작업을 반복하는 반복문을 사용하여 파일 전체를 읽도록 구현하는 것이 좋다.

file = open('./input/엄마돼지아기돼지.txt','rt')

while True:
    str = file.read(5)
    if not str :
        break
    print(str,end='')

file.close()

# file.read(5)는 파일로부터 최대 5글자를 읽어들임
# 파일이 종료되어 더이상 읽어들일 글자가 없으면 빈 문자열('')을 읽어들임

print()
print()

# 2) readline() 메소드
# 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드
# 파일이 종료되어 더이상 읽어들일 글자가 없으면 빈 문자열('')을 읽어들임
# 반복문을 이용해서 여러번 읽어 들여야 파일 전체를 읽을 수 있다.

file = open('./input/hello.txt','rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str,end='')
file.close()

# 3) readlines() 메소드
# line하나가 아니라 전체 lines를 모두 읽어 각 line단위로 리스트에 저장하는 메소드

file = open('./input/hello.txt','rt')
line_list = file.readlines()
print(line_list)
# 결과: ['안녕하세요\n', '반갑습니다\n', 'hello.txt 파일이 생성되었습니다.\n', 'Hello\n', 'Nice to meet you\n']

count = 0
for line in line_list:
    for str in line:
        if str == '다':
            count += 1

print(f'다는 {count}번 있습니다.')