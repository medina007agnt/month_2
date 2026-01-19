class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):#строковая
        return f"Money object amount = {self.amount}"

    def __eq__(self, other):#equal -> сравнение 
        if self.amount != other.amount:
            return False
        return True

money_medina = Money(100)
money_mediana = Money(100)
print(money_medina)
print(money_mediana == money_medina)


