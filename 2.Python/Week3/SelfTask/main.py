from Payment import PaymentMethod

class PaymentCash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} by cash.")

    def recipt(self):
        return super().recipt() + "Paid by Cash"

class PaymentCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} by card.")

    def recipt(self):
        return super().recipt() + "Paid by Card"

card = PaymentCard()

card.pay(100)
print(card.recipt())