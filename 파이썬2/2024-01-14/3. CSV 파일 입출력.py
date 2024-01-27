# CSV 파일 입출력

# 1. CSV 파일이란?
# 데이터베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식
# 내부는 실제 쉼표(,)를 이용해서 모든 항목이 구분되어 있으며
# 쉼표로 구성된 각 항목들이 테이블을 구성하는 데이터가 되는 형식
# 메모장에서는 텍스트로 받거나 적을 수 있고, 엑셀에서는 각 셀로 나누어서 보인다.

# 2. CSV 파일 읽기
# 현재 한국의 전자정부 프레임워크, 데이터를 기록할 때 대부분 .csv파일로 저장한다
# 단점: 한국,일본만 사용함

# 1) 한 줄에 한 데이터가 있기 때문에 readline()메소드로 한 줄 씩 읽는다.
# 2) 쉼표(,)로 분리하기 위해서 split() 메소드를 이용

student_list = []
with open('./input/학생명단.csv','rt') as file:
    file.readline() # 학번, 이름, 주소, 연락처
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)

# 학생 정보를 student 리스트에 저장하고, student_list 리스트에 student 리스트를 저장

# CSV 파일을 사용하다 보면 간혹 큰 따옴표(")를 이용해서 텍스트를 묶는 경우가 있다.
# 큰 따옴표를 제거하기 위해서 추가로 strip() 메소드를 사용해야 함

member_list = []
with open('./input/회원명단.csv','rt') as file:
    file.readline() # 학번, 이름, 주소, 연락처
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member_list.append(member)
print(member_list)


# 3. csv 모듈로 CSV 파일 생성하기
# import csv를 통해서 csv파일을 쉽게 처리할 수 있는 csv모듈을 사용

# w모드로 열고 생성된 파일 객체를 csv.writer()메소드에 전달
# csv 파일을 생성할 수 있는 객체를 생성한 후 writerow()메소드를 호출하면 csv 파일에 데이터를 저장 가능

# delimiter(구분자)란, 데이터 파일에서 각 열(column)이나 필드(field)를 구분하는 문자
# delimiter 매개변수를 쉼표로 지정하여 csv.reader 함수를 호출하면 쉼표로 구분된 csv파일을 읽을 수 있다.
# delimiter는 콜론(:),세미콜론(;),파이프(|)등 다양한 문자로 지정 가능하다.

import csv

with open('./output/차량관리_01.csv','w') as file:
    csv_maker = csv.writer(file,delimiter=',')
    csv_maker.writerow([1,'08러1234','2024-01-14 16:10'])
    csv_maker.writerow([2,'25다1234','2024-01-14 16:20'])
    csv_maker.writerow([3,'28하1234','2024-01-14 16:30'])

print('차량관리_01.csv 파일이 생성되었습니다.')

# 생성된 csv파일을 보면 불필요한 라인이 하나씩 추가되어 있음
# 이를 막기 위해 새로운 라인을 추가하지 못하도록 newline옵션을 사용
# 줄 바꿈이 되지 않도록 newline 옵션에 빈 문자열을 지정하고 이를 코드에 반영

import csv

with open('./output/차량관리_02.csv','w',newline='') as file:
    csv_maker = csv.writer(file,delimiter=',')
    csv_maker.writerow([1,'08러1234','2024-01-14 16:10'])
    csv_maker.writerow([2,'25다1234','2024-01-14 16:20'])
    csv_maker.writerow([3,'28하1234','2024-01-14 16:30'])

print('차량관리_02.csv 파일이 생성되었습니다.')