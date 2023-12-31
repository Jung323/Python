class Person:
    population = 0
    def __init__(self,name):
        self.name = name
        Person.population += 1
    def __str__(self):
        return f'{self.name} is born'

    @classmethod
    def get_population(cls):
        return cls.population

    def __del__(self):
        Person.population -= 1
        print(f'{self.name} is dead')

man = Person('james')
print(man) #결과: james is born
woman = Person('emily')
print(woman) #결과: emily is born


print(f'전체 인구수 : {Person.get_population()}명')


del man
print(f'전체 인구수 : {Person.get_population()}명')