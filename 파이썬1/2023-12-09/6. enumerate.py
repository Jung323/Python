# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태로 함께 추출
# for item in enumerate([리스트]) :
#   반복실행문

for item in enumerate(['가위','바위','보']) :
    print(item)

print()

for idx, element in enumerate(['가위','바위','보']) :
    print(idx,'/',element)

