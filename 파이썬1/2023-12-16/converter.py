# MILE, POUND 단위 변환에서 사용할 함수

MILE = 0.621371 #1kg = 0.621371mile
POUND = 0.002205 #1g = 0.002205pound

def kilometer_to_mile(kilometer): # 킬로미터를 마일로 변환하는 함수
    return kilometer * MILE

def gram_to_pound(gram): # 그램을 파운드로 변환하는 함수
    return gram * POUND

