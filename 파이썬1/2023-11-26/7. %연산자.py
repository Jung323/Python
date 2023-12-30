# %연산자
name = 'KoreaIT'
print('나의 학원은 %s입니다.' % name) #결과: 나의 학원은 KoreaIT입니다. / %s : string
print('나의 학원은 ',name,'입니다.',sep='') #결과: 나의 학원은 KoreaIT입니다.
print('나의 학원은 '+ name + '입니다.')#결과: 나의 학원은 KoreaIT입니다.

height = 158.8
print('내 키는 %fcm입니다.' % height) #결과: 내 키는 158.800000cmd입니다. / %f : float

weight = 46.32
print('내 몸무게는 %.1fkg입니다.' % weight) #결과: 내 몸무게는 46.3kg입니다. / %.1f : 반올림해서 1째자리까지 나타냄

year, month, day = 2023, 11, 26
print('오늘은 %d년 %d월 %d일 입니다.' %(year,month,day)) #결과: 오늘은 2023년 11월 26일 입니다. / %d : 정수형(int) decimal(십진법)
