# Challenge 3: Implement the Complete Student Class
# In this challenge, you will implement a student class
# Problem statement

# Implement the complete Student class by completing the tasks below

# Task

# Implement the following properties as private:

# • name
# • rollNumber
# Include the following methods to get and set the private properties above:

# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()

class Student:
    def __init__(self):
        self._name = ""
        self._rollNumber = ""

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber


name = input("Enter the student's name: ")
rollNumber = input("Enter the student's roll number: ")

student = Student()


student.setName(name)
student.setRollNumber(rollNumber)


studentName = student.getName()
studentRollNumber = student.getRollNumber()

print("Student Name:", studentName)
print("Student Roll Number:", studentRollNumber)