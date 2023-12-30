while True: #무한루프
    city = input('대한민국의 수도는 어디인가요? : ')
    city = city.strip() # strip : 문자열에서 양쪽 끝에 있는 공백문자를 제거한다.
    if city == '서울' or city == 'seoul' or city == 'SEOUL' :  # 대소문자를 모두 정답처리
        print('정답입니다')
        break
    else:
        print('오답입니다. 다시 시도하세요.')