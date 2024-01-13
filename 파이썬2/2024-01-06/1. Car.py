class Car:
    max_oil = 50 # 최대 주유량

    def __init__(self,oil):
        self.oil = oil

    def add_oil(self,oil: int):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil: # 주유 후 최대 주유량 초과상태이면
            self.oil = Car.max_oil # 현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')

car = Car(0)
car.car_info() #결과: 현재 주유 상태 : 0
car.add_oil(40)
car.car_info() #결과: 현재 주유 상태 : 40
car.add_oil(50)
car.car_info() #결과: 현재 주유 상태 : 50

print()
class Hybrid(Car): #자식클래스에서 부모클래스를 상속받음
    max_battery = 30

    def __init__(self,oil:int,battery:int):
        super().__init__(oil)
        self.battery = battery

    def charge(self,battery:int):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery :
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전 상태 : {self.battery}')

car = Hybrid(0,0)
car.add_oil(100)
car.charge(40)
car.hybrid_info()
# 결과:
# 현재 주유 상태 : 50
# 현재 충전 상태 : 30