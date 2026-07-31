class Temperature:
    def __init__(self, v):
        if v < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__temp = v

    @property
    def celcius(self): return self.__temp
    @celcius.setter
    def celcius(self, v):
        if v < -273.15:
            raise ValueError("Temparature Below absolute zero!")
        self.__temp = v

    @property
    def Farenheit(self): return self.__temp * 9 / 5 + 32
    @Farenheit.setter
    def Farenheit(self, v):
        if v < -459.67:
            raise ValueError("Temperature below absolute zero!")
        self.__temp = (v - 32) * 5 / 9


kitchen = Temperature(33)

print(kitchen.celcius)
print(kitchen.Farenheit)
kitchen.celcius = 123
print(kitchen.Farenheit)