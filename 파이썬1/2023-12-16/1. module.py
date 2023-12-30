# 1. module(모듈)이란
# 한마디로 파이썬 파일(.py)
# 언제든지 사용할 수 있도록 변수나 함수 또는 클래스를 모아 놓은 파일

# 2. 모듈 생성
# converter.py 생성

# 3. 모듈의 사용
# 반드시 같은 디렉터리(폴더)에 있어야 한다.
# 모듈에 저장된 함수를 사용하는 방법



# (1) 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때
# 예) import 모듈

import converter

mile = converter.kilometer_to_mile(150) #모듈함수.함수() 형식
print(f'150km = {mile}mile') #결과: 150km = 93.20565mile

pound = converter.gram_to_pound(1000)
print(f'1000g = {pound}pound') #결과: 1000g = 2.205pound

# (2) 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법

# 예) from 모듈 import 함수
# 예) from 모듈 import 함수1,함수2
# 예) form 모듈 import *


# 모듈은 가져오지 않고 특정 함수만 가져온다.
from converter import kilometer_to_mile
mile = kilometer_to_mile(200)
print(f'200km = {mile}mile') #결과: 200km = 124.27420000000001mile


# 모듈은 사용하지 않고 모듈의 모든 함수를 가져온다.
from converter import *
pound = gram_to_pound(10000)
print(f'10000g = {pound}pound') #결과: 10000g = 22.05pound


# 4. 별명 사용하기
# 모듈이나 함수를 import하는 경우에 원래 이름 대신 별명 alias를 지정하고 사용
# 모듈이나 함수의 이름이 긴 경우에 주로 짧은 별명을 지정하고 긴 본래 이름 대신 사용
# 별명을 지정할 떄는 as 키워드를 사용


# converter 모듈에 cvt라는 별명을 지정
import converter as cvt
mile = cvt.kilometer_to_mile(150)
print(f'150km = {mile}') #결과: 150km = 93.20565

pound = cvt.gram_to_pound(1000)
print(f'1000g = {pound}') #결과: 1000g = 2.205

# 함수에도 별명을 지정가능
from converter import kilometer_to_mile as k_to_m

mile = k_to_m(150)
print(f'150km = {mile}')#결과: 150km = 93.20565

