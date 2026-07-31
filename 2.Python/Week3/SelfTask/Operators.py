import math

class Fraction:
    def __init__(self, a, b):
        if (b == 0):
            raise ValueError("Dominator canot be zero!")
        gcd = math.gcd(a, b)
        self.__num = a // gcd
        self.__den = b // gcd

    def __add__(self, fr):
        new_a = self.__num*fr._Fraction__den + fr._Fraction__num*self.__den
        new_b = self.__den * fr._Fraction__den

        gcd = math.gcd(new_a, new_b)
        return Fraction(new_a // gcd, new_b // gcd)

    def __eq__(self, fr):
        gcd1 = math.gcd(self.__num, self.__den)
        gcd2 = math.gcd(fr._Fraction__num, fr._Fraction__den)

        if (self.__num // gcd1 == fr._Fraction__num // gcd2 
            and self.__den // gcd1 == fr._Fraction__den // gcd2):
            return True
        else:
            return False
        
    def __ne__(self, fr):
        gcd1 = math.gcd(self.__num, self.__den)
        gcd2 = math.gcd(fr._Fraction__num, fr._Fraction__den)

        if (self.__num // gcd1 == fr._Fraction__num // gcd2 
            and self.__den // gcd1== fr._Fraction__den // gcd2):
            return False
        else:
            return True

    def __lt__(self, fr):
        temp1 = self.__num * fr._Fraction__den
        temp2 = self.__den * fr._Fraction__num

        return temp1 < temp2
        
    def __le__(self, fr):
        temp1 = self.__num * fr._Fraction__den
        temp2 = self.__den * fr._Fraction__num

        return temp1 <= temp2

    def __str__(self):
        gcd = math.gcd(self.__num, self.__den)

        a, b = self.__num // gcd, self.__den // gcd
        return str(a) + "/" + str(b)

Biba = Fraction(10,20)
Boba = Fraction(3, 4)
Baba = Fraction(3, 4)

print(Biba == Boba)
print(Biba > Boba)
print(Baba >= Boba)
print(str(Biba + Boba))