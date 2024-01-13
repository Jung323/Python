# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서
# '꿀'이라는 글자가 몇번 나오는지 찾는 프로그램입니다.

# 방법1
file = open('./input/엄마돼지아기돼지.txt','rt')
list_lines = file.readlines()
print(list_lines)

count = 0
for line in list_lines:
    for str in line:
        if str == '꿀':
            count += 1
print(f'엄마돼지 아기돼지 동요에 꿀이라는 단어는 {count}번 나옵니다.')

# 방법2
file = open('./input/엄마돼지아기돼지.txt','rt')
str2 = file.read()
print(f'엄마돼지 아기돼지 동요에 꿀이라는 단어는 {str2.count('꿀')}번 나옵니다.')