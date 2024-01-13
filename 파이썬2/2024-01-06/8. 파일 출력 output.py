# 파일 출력 output
# 1. 텍스트 파일 생성하기
file = open('./output/hello.txt','wt',encoding='utf-8')

file.write('안녕하세요')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
file.write('hello.txt파일이 생성되었습니다.\n')

file.close()

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a모드 (append)
file = open('./output/hello.txt','at')

file.write('hello\n')
file.write('Nice to meet you\n')
print('hello.txt.파일에 내용이 추가되었습니다.')
file.close()

# 한글 이름 파일 utf-8 문서 작성
import codecs

file = codecs.open('./output/한글파일.txt','w','utf-8')
file.write('나는 오늘 학원에 갔습니다.')
file.close()
print('한글파일이 만들어졌습니다.')