# 학생 리스트를 선정, 딕셔너리 요소를 가진 리스트

students = [
    {'name': '연하진', 'korean': 92, 'math': 96, 'science': 98},
    {'name': '구지연', 'korean': 76, 'math': 94, 'science': 90},
    {'name': '나선주', 'korean': 98, 'math': 96, 'science': 92},
    {'name': '윤아린', 'korean': 95, 'math': 98, 'science': 98},
    {'name': '윤명월', 'korean': 64, 'math': 88, 'science': 92}
]

# 학생을 한번씩 반복
print('이름','    총점','평균',sep='\t\t')
for student in students:
    # 점수의 총합과 평균을 구함
    score_sum = student['korean'] + student['math'] + student['science']
    score_average = score_sum / 3
    # 출력
    print(student['name'],score_sum,score_average,sep='\t\t')