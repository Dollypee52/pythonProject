class Account:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        self.balance = 0

    def balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= 0:
                self.balance -= amount
                return self.balance

    def transfer(self, amount, other):
        self.balance -= amount
        return self.balance
