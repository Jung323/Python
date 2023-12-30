# num_list = []
#
# while True:
#     n2 = int(input('숫자를 입력하세요: '))
#     if n2 == -1 :
#         num_list.sort()
#         print(f'입력한 숫자 중에서 가장 큰 수는 {num_list[-1]}입니다.')
#         break
#     else:
#         num_list.append(n2)


num_list = []

while True:
    n2 = int(input('숫자를 입력하세요: '))
    if n2 == -1:
        print('종료합니다.')
        print(f'입력한 숫자 중에서 가장 큰 수는 {max(num_list)}입니다.')
        break
    else:
        num_list.append(n2)
