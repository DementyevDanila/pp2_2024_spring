class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, cash):
        self.balance += cash
        print(f"Now in deposit {self.balance} $")

    def withdraw(self, cash):
        if self.balance - cash >= 0:
            self.balance -= cash
            print(f"Now in deposit {self.balance} $")
        else:
            print(f"Suddenly, there is no enough money to do this operation")

user = Account("Admin", 200)

user.deposit(100)
user.withdraw(500)
user.withdraw(300)