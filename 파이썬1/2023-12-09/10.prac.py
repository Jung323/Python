print('점수를 입력하세요.')
print('더이상 점수가 없으면 음수를 아무거나 입력하세요.')

scores = []

while True:
    total = 0
    score = int(input('점수를 입력하세요: '))
    if score < 0 :
        break
    else:
        scores.append(score)
    # for s in scores:
    #     total += s
    # ave_score = total / len(scores)
    ave_score = sum(scores)/len(scores)
    max_score = sorted(scores)[-1]
    min_score = sorted(scores)[0]
    # max_score = max(scores)
    # min_score = min(scores)
print(f'평균 = {ave_score}, 최대 = {max_score}, 최소 ={min_score}')





