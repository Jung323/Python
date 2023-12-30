#5자리로 구성된 학번 '31025'를 학년,반,번호로 나누어 출력하는 프로그램을 구현하세요.
#실행 예) 3학년 10반 25번

student= '31025'

#답안1
print(student[0:1]+'학년 '+student[1:3]+'반 '+student[3:5]+'번')

print()

#답안2
grade_no = student[0:1]
class_no = student[1:3]
stu_no = student[3:5]
print(grade_no, '학년', class_no, '반', stu_no, '번')

print()
#전체 차량번호에서 뒤에 숫자 4자리만 출력하는 프로그램을 구현하세요.
#전체 차량번호는 '서울2가 1234','10가 1234', '288가 1234'와 같이 다르지만 모두 차량번호 4자리는 '1234'입니다.
#실행 예) 서울2가 1234의 차량번호 4자리는 1234입니다.

#답안1
car1 = '서울2가 1234'
car2 = '10가 1234'
car3 = '288가 1234'
print(car1+'의 차량번호 4자리는 '+ car1[-4:]+'입니다.')


print()
답안2
car1 = '서울2가 1234'
#
car2 = '10가 1234'
car3 = '288가 1234'
car_list=[car1,car2,car3]
#print(car_list)


i=0
while i<3:
    print(car_list[i]+'의 차량번호 4자리는 '+car_list[i][-4:]+'입니다.')
    i=i+1