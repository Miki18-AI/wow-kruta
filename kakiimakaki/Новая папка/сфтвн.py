class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self,value):
        if value < 0 :
            return "Error dollars"
        elif isinstance(value, str):
            return "Error dollars"
        else:
            return self.dollars
    @property
    def cents(self):
        return self.total_cents % 100
    @cents.setter
    def cents(self, value):
        if isinstance(value, str):
            print("Error cents")
        elif value < 0 :
            print("Error cents")
        else:
            return self.cents
cash = Money(34,77)
print(cash.dollars)
print(cash.cents)
cash.cents = "hello"