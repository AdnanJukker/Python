class Employee:
    language = "Python"
    salary = 100000

    def __init__(self): #dunder method, constructor
        print("I am creating an employee object.")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

Adnan = Employee()
Adnan.greet()

