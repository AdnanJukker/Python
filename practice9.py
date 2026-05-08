# class programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = programmer("Adnan",100000,1234)
# print(p.company)
# print(p.name,p.salary,p.pin)

# class calaculator:
#     def __init__(self,num):
#         self.num = num

#     def square(self):
#         print("The square of",self.num,"is",self.num * self.num)

#     def cube(self):
#         print("The cube of",self.num,"is",self.num * self.num * self.num)
    
#     def sqrt(self):
#         print("The square root of",self.num,"is",self.num ** 1/2)
    
# a = calaculator(8)
# a.square()
# a.cube()
# a.sqrt()   


# class demo:
#     a =4
# o = demo()
# print(o.a)  #prints class attribute because instance attribute is not defined
# o.a = 0 #instance attribute is created and assigned value 0, it will override the class attribute
# print(o.a)    #prints instance attribute because it is defined, it will override the class attribute
# print(demo.a) #prints class attribute because it is not overridden by instance attribute    

# class calaculator:
#     def __init__(self,num):
#         self.num = num

#     def square(self):
#         print("The square of",self.num,"is",self.num * self.num)

#     def cube(self):
#         print("The cube of",self.num,"is",self.num * self.num * self.num)
    
#     def sqrt(self):
#         print("The square root of",self.num,"is",self.num ** 1/2)

#     @staticmethod
#     def hello():
#         print("Hello, welcome to the calculator!")
    
# a = calaculator(8)
# a.hello()  #static method can be called using instance or class name
# a.square()
# a.cube()
# a.sqrt()  

import random

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def booking(self, frm, to):
        print(f"Your ticket for train {self.trainNo} from {frm} to {to} has been booked.")

    def getStatus(self):
        print(f"Train {self.trainNo} is on time.")

    def fare(self, frm, to):
        print(f"The fare for train {self.trainNo} from {frm} to {to} is {random.randint(100, 1000)}.")

t = Train(12345)
t.booking("Karachi", "Lahore")
t.getStatus()
t.fare("Karachi", "Lahore")