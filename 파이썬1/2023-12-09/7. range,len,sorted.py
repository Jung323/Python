# range() : 전달된 인수값에 따라 시퀀스 자료형의 데이터를 생성
# 1) range(stop)
# : 0부터 stop사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는 0 <= n < stop

# 2) range(start,stop)
# : start부터 stop사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는 start <= n < stop

# 3) range(start,stop,step)
# : start부터 stop사이의 정수중에서 step만큼의 차이가 발생


print(list(range(10)))
print(list(range(1,11)))
print(list(range(0,30,5)))
print(list(range(0,-10,-1)))
print(list(range(0)))
print(list(range(1,0)))


print()
# len() : 함수에 전달된 객체의 길이(항목 수)를 반환
li = ['a','b','c','d','e']
print(len(li))


d = {'a':'apple','b':'banana'}
print(len(d)) # 결과 : 2 / 딕셔너리는 'key:value'로 구성된 한 쌍을 하나의 데이터로 본다.

print(len(range(10)))
print(len(range(1,11)))

print()

# range() 함수와 리스트의 길이를 구하는 len()함수를 함께 사용하면 리스트의 인덱스를 생성 가능

seasons = ['봄','여름','가을','겨울']
seasons_eng = ['spring','summer','fall','winter']

#len(seasons)
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')




# sorted() : 전달된 반복가능객체의 오름차순 정렬 결과를 반환

print()
my_list = ['b','c','a','d']
print(sorted(my_list)) # 결과: ['a', 'b', 'c', 'd']

my_list2 = [6,3,1,2,5,4]
print(sorted(my_list2)) # 결과: [1, 2, 3, 4, 5, 6]
print(sorted(my_list2,reverse = True)) # 결과:[6, 5, 4, 3, 2, 1]