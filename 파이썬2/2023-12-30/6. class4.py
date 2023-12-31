def create_student(name,korean,math,english,science):
    return {
        'name':name,
        'korean':korean,
        'math':math,
        'english':english,
        'science':science
    }

# 학생을 처리하는 함수를 선언
def student_get_sum(student):
    return student['korean'] + student['math'] + student['english'] + student['science']

# 평균 구하기
def student_get_average(student):
    return student_get_sum(student) / 4

# 학생 정보 출력
def student_to_string(student):
    return print(f'{student['name'],student_get_sum(student),student_get_average(student)}')

students = [
    create_student('연하진', 92, 98, 96, 98),
    create_student('구지연', 76, 96, 94, 90),
    create_student('나선주', 98, 92, 96, 92),
    create_student('윤아린', 95, 98, 98, 98),
    create_student('윤명월', 64, 88, 92, 92)
]

# 학생을 한명씩 반복
print('이름','  총점','평균',sep='\t\t')
for student in students :
    student_to_string(student)