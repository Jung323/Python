
# 1. 가격과 수량을 입력할 때 숫자가 아닌 값이 입력되면 "올바른 숫자를 입력하세요." 라는 메시지가 나와야 한다.
# 2. 가격이 음수인 경우 "가격은 음수일 수 없습니다."라는 메시지가 나와야 한다.
# 3. 수량이 음수인 경우 "수량은 음수일 수 없습니다."라는 메시지가 나와야 한다.


# try:
#     price = float(input('제품의 가격을 입력하세요: '))
#     quantity = int(input('제품의 수량을 입력하세요: '))
#     if price >= 0 :
#         print(f'입력된 가격은 {price}입니다.')
#     else:
#         print('가격은 음수일 수 없습니다.')
#
#     if quantity >= 0:
#         print(f'입력된 수량은 {quantity}입니다.')
#     else:
#         print('수량은 음수일 수 없습니다.')
#
# except ValueError:
#     print('올바른 숫자를 입력하세요.')
# except Exception as e:
#     print('오류 발생',e)




# raise를 사용
try:
    price = float(input('제품의 가격을 입력하세요: '))
    quantity = int(input('제품의 수량을 입력하세요: '))

    if price < 0:
        raise ValueError('가격은 음수일 수 없습니다.')
    if quantity < 0:
        raise ValueError('수량은 음수일 수 없습니다.')

except ValueError as e:
    print(e,'올바른 숫자를 입력하세요.')

except Exception as e:
    print('오류 발생',e)

