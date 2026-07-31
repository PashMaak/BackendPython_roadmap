class Employee:
    def __init__(self, money):
        if (money < 0):
            raise ValueError("Employee cannot have negative salary!")
        self.__salary = money

    @property
    def salary(self): return self.__salary
    @salary.setter
    def salary(self, money):
        if (money < 0):
            raise ValueError("Employe cannot have negative salary!")
        self.__salary = money

    def bonus(self): return self.__salary*0.05

class Manager(Employee):
    def __init__(self, money): super().__init__(money)

    def bonus(self):
        return super().bonus() * 2 # Additional bonus to manager

    # @property
    # def salary(self):
    #     return super().salary
    # @salary.setter
    # def salary(self, money):
    #     return super().salary(money)
        

class Developer(Employee):
    def __init__(self, money): super().__init__(money)

    def bonus(self):
        return super().bonus()

    # @property
    # def salary(self):
    #     return super().salary
    # @salary.setter
    # def salary(self, money):
    #     return super().salary(money)

Aboba = Manager(500)
Bababoy = Developer(130)

print(Aboba.salary + Aboba.bonus())
print(Bababoy.salary + Bababoy.bonus())