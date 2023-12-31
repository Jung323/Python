# 떡볶이: 3000, 순대: 3000, 튀김: 500, 김밥: 2000

# 방법1)
class Shop:
    total = 0
    @classmethod
    def sales(cls,menu,count):
        cls.menu = menu
        cls.count = count
        if cls.menu == '떡볶이':
            cls.price = 3000
        elif cls.menu == '순대':
            cls.price = 3000
        elif cls.menu == '튀김':
            cls.price = 500
        elif cls.menu == '김밥':
            cls.price = 2000
        Shop.total += cls.price*cls.count

Shop.sales('떡볶이',1)
Shop.sales('김밥',2)
Shop.sales('튀김',5)
print(f'매출: {Shop.total}원')

# 방법2)
class Shop:
    total = 0
    menu_list = [{'떡볶이':3000},{'순대':3000},{'튀김':500},{'김밥':2000}]

    @classmethod
    def sales(cls,food,count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total += (menu[food]*count)

Shop.sales('떡볶이',1)
Shop.sales('김밥',2)
Shop.sales('튀김',5)
print(f'매출: {Shop.total}원')
