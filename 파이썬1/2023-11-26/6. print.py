# print() 함수
# end : value 출력 후 출력할 문자
# end 속성을 사용하지 않고 print() 함수를 사용하면 출력 후 자동으로 줄바꿈이 진행
# sep : 출력할 value의 구분자
# sep 속성을 사용하지 않고 print()함수를 사용하면 출력 대상은 공백으로 구분

print('재미있는','파이썬') #결과: 재미있는 파이썬/ 콤마(,)로 구분된 출력대상은 공백으로 구분
print('Python','Java','C',sep=';') #결과: Python;Java;C / sep속성으로 구분됨

print()
print('영화 타이타닉')
print('평점',end=':')
print('5점') #value 출력 후 end 속성 출력. 줄바꿈이 되지 않는다.
