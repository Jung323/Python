# format() 메소드
# format() 메소드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식

print('My name is {}'.format('james')) #결과: My name is james
print('My name is {name}'.format(name='james')) #결과: My name is james


print('My name is {}. I\'m {} years old'.format('james',25)) #결과: My name is james. I'm 25 years old
print('My name is {1}. I\'m {0} years old'.format('james',25)) #결과: My name is 25. I'm james years old / 인덱스가 지정가능하다.
print('My name is {name}. I\'m {age} years old'.format(name='james',age=25)) #결과: My name is james. I'm 25 years old