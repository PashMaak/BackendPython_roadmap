class BankAccount:
    def __init__(self, money):
        if (money < 0):
            raise ValueError("Negative balance error!")
        self.__balance = money

    @property
    def balance(self): return self.__balance
    @balance.setter
    def balance(self, money):
        if (money < 0):
            raise ValueError("Negative balance error!")
        self.__balance = money

    def deposit(self, amount):
        if (amount < 0):
            raise ValueError("Error you cannot deposit negative amount of money!")
        self.__balance += amount
    def withdraw(self, amount):
        if (amount < 0):
            raise ValueError("You cannot withdraw negative amount of money!")
        if (self.__balance - amount < 0):
            raise ValueError("You cannot withdraw more than you have!")
        self.__balance -= amount

acc = BankAccount(100)

print(acc.balance)      # 100

acc.deposit(50)

print(acc.balance)      # 150

acc.withdraw(30)

print(acc.balance)      # 120