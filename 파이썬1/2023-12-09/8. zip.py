# zip() : 전달된 여러 개의 반복 가능 객체의 각 요소를 튜플로 묶어서 반환
# 전달된 반복 가능 객체들의 길이가 서로 다르면 길이가 짧은 반복 가능 객체 기준으로 동작

names = ['james','emily','amanda']
scores = [60,70,80]
for student in zip(names,scores) :
    print(student)

print()


# 투퓰은 언패킹이 가능하므로 다음과 같은 모습으로 구성 가능

for name, score in zip(names,scores) :
    print(f'{name}의 점수는 {score}입니다.')

print()

seasons = ['봄', '여름', '가을', '겨울']
seasons_eng = ['spring', 'summer', 'fall', 'winter']
for a,b in zip(seasons, seasons_eng):
    print(f'{a}의 계절은 영어로 {b}입니다.')
