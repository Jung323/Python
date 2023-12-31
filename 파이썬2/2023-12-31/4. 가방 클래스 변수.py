# 가방을 만들 때마다 만들어진 가방이 몇 개인지 계산할 수 있는 가방 클래스

class Bag:
    count = 0 # 클래스 변수

    def __init__(self): # 생성자가 실행될 때마다 증가
        Bag.count += 1

    @classmethod
    def sell(cls): # 판매시 감소
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

print(f'현재 가방 {Bag.remain_bag()}')
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 {Bag.remain_bag()}')
bag4 = Bag.sell()
bag5 = Bag.sell()
print(f'현재 가방 {Bag.remain_bag()}')