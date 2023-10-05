# Challenge 4: Implement a Banking Account
# In this challenge, you will implement a banking account using the concepts of inheritance.
# Problem statement

# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate


account = Account("Ashish", 5000)
print(f"Account title: {account.title}")
print(f"Account balance: {account.balance}")


savingsAccount = SavingsAccount("Ashish", 5000, 5)
print(f"Savings Account title: {savingsAccount.title}")
print(f"Savings Account balance: {savingsAccount.balance}")
print(f"Savings Account interest rate: {savingsAccount.interestRate}")
