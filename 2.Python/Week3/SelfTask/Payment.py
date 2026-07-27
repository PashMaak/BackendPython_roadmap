from  abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def pay(amount):
        pass

    def recipt(self):
        return "Recipt generated "
