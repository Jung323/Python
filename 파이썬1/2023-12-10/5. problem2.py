# 우리 학교 성적 프로그램은 다음과 같이 쉼표로 구분된 문자열 형식으로 학생 이름과 성적이 입력됩니다.
# 이 데이터를 각각 name과 score 변수에 저장하는 프로그램을 구현하세요.

student = input('학생 이름과 성적을 입력하세요. 예)"김철수",85: ')
name = student.split(',')[0].replace('"','')
score = student.split(',')[1]
print(f'이름은 {name}이고, 점수는 {score}입니다.')

