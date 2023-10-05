# Challenge 2: Implement a Calculator Class
# In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.

# Problem statement Write a Python class called Calculator by completing the tasks below:

# Task 1

# Initializer

# Implement an initializer to initialize the values of num1 and num2. Properties

# • num2
# Task 2

# Methods

# • add() is a method that returns the sum of num1 and num2.
# • subtract() is a method that returns the subtraction of num1 from num2.
# • multiply() is a method that returns the product of num1 and num2.
# • divide() is a method that returns the division of num2 by num1.
# Input - Pass numbers (integers or floats) in the initializer.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1

num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))


obj = Calculator(num1, num2)


addition = obj.add()
subtraction = obj.subtract()
multiplication = obj.multiply()
division = obj.divide()


print(addition)
print(subtraction)
print(multiplication)
print(division)