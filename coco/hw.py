class BankAccount:

    balance = 0
    name = ''

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __add__(self, other):
        return self.balance + other.balance

    def __repr__(self):
        return self.name + ':' + str(self.balance)


class SavingsAccount(BankAccount):
    interest_rate = 0.1
    balance = 0
    name = ''

    def add_interest(self):
        self.balance += self.interest_rate


b = BankAccount()
b.balance = 1000
b.name = 'Susan'
s = SavingsAccount()
s.interest_rate = 0.3
print(b.balance * s.interest_rate)
print(b)