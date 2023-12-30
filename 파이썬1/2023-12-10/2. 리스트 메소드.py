# 2 리스트 메소드
# 1) append()
# 리스트의 끝에 인수로 전달된 인수를 추가

my_list = ['apple','banana']
my_list.append('cherry')
print(my_list) #결과 : ['apple', 'banana', 'cherry']

# 2) extend()
# 리스트에 다른 리스트나 튜플과 같은 반복가능객체를 추가하여 기존 리스트를 확장

my_list = ['apple','banana']
my_list.extend(['cherry','mango'])
print(my_list) #결과 :['apple', 'banana', 'cherry', 'mango']

my_list = ['apple','banana']
my_list += ['cherry','mango']
print(my_list) #결과: ['apple', 'banana', 'cherry', 'mango']

# 3) insert()
# 리스트의 특정 인덱스에 데이터를 추가
my_list = ['apple','banana']
my_list.insert(0,'cherry')
print(my_list) #결과 : ['cherry', 'apple', 'banana']

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제

my_list = ['apple','banana']
my_list.clear()
print(my_list) #결과: []

my_list = ['apple','banana']
my_list = []
print(my_list) #결과: []

# 5) pop()
# 리스트의 마지막 요소가 반환되면서 삭제

my_list = ['apple','banana']
item = my_list.pop()
print(item) #결과: banana
print(my_list) #결과: ['apple']

# pop(idx) : 인덱스를 지정한 경우에는 해당 인덱스 요소를 반환하면서 삭제됨

my_list = ['apple','banana']
item = my_list.pop(0)
print(item) #결과: apple
print(my_list) #결과: ['banana']

# 6) remove()
# 인수로 전달된 값과 동일한 요소를 찾아서 제거. 동일한 요소가 여러 개인 경우에는 첫번쨰 요소가 제거
my_list = ['apple','banana','cherry','mango']
my_list.remove('cherry')
print(my_list) #결과: ['apple', 'banana', 'mango']

my_list = ['apple','banana','cherry','mango','cherry','cherry']
my_list.remove('cherry')
print(my_list) #결과: ['apple', 'banana', 'mango', 'cherry', 'cherry']

