# Handling a Bank Account
# In this challenge, you will define methods for handling a bank account using concepts of inheritance.

# Problem statement

# In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.

# The initializers for both classes have been defined for you.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100



account = Account("Ashish", 2000)
account.deposit(500)
print(account.getBalance())  

account.withdrawal(500)
print(account.getBalance())  

savingsAccount = SavingsAccount("Ashish", 2000, 5)
print(savingsAccount.interestAmount())  