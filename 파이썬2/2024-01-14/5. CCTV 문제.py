# 다음은 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.

# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다
# 5번째 데이터가 카메라 대수입니다.

# 실행 예 :
# 서울특별시 마포구에 설치된 CCTV는 총 2167대 입니다.
# hint : 카메라 대수는 int 타입으로 형변환 해줘야 한다.

import csv
cctv_file = open('./input/cctv.csv','r')
cctv_file_reader = csv.DictReader(cctv_file)

count = 0
for row in cctv_file_reader:
    # print(row['카메라대수'])
    count += int(row['카메라대수'])
print(f'서울특별시 마포구에 설치된 CCTV는 총 {count}대 입니다.')

# 강사님 코드
with open('./input/cctv.csv', 'r') as csvfile:
    datas = csv.DictReader(csvfile)
    total_cctv = 0
    for data in datas:
        total_cctv += int(data['카메라대수'])

print(f'서울특별시 마포구에 설치된 CCTV는 총 {total_cctv}대 입니다.')