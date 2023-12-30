months = [31,28,31,30,31,30,31,31,30,31,30,31]
for month,day in enumerate(months):
    print(f'{month+1}월 = {day}일')

print()

month = 1
for item in months:
    print(f'{month}월 = {item}일')
    month += 1

print()

months_eng = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

for idx, day in enumerate(months):
    print(f'{months_eng[idx]} = {day}일')

    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

    for idx, color in enumerate(rainbow):
        print(f'무지개의 {idx + 1}번째 색은 {color}입니다.')
