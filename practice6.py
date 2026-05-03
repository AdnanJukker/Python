#qq1
s = int(input("Enter your age: "))

if s>=18:
    print("YES")
else:
    print("No")

print("End of program")   

#q1
a1 = int(input("Enter the number1: "))
a2 = int(input("Enter the number2: "))
a3 = int(input("Enter the number3: "))
a4 = int(input("Enter the number4: "))

if (a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1:", a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2:", a2)
elif (a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3:", a3)
elif (a4>a1 and a4>a2 and a4>a3):
    print("greatest number is a4:", a4)
else:
    print("all are same")    

print("End of program")   

#q2

marks1 = int(input("Enter marks 1: ")) 
marks2 = int(input("Enter marks 2: ")) 
marks3 = int(input("Enter marks 3: ")) 

total_percentage = (100*(marks1 + marks2 + marks3))/300

if (total_percentage>= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("your are pass",total_percentage)
else:
    print("You failed",total_percentage)  

#q3

a1 = "make a lot of money"
a2 = "buy now"
a3 = "subscribe this"
a4 = "click this"

message = input("Enter your message: ")

if((a1 in message) or (a2 in message) or (a3 in message) or (a4 in message)):
    print("this is a spam message")
else:
    print("this is not a spam message")    

#q4
user =  input("Enter your name: ")
if (len(user)<10):
    print("you have less characters")
else:
    print("you have more than 10 characters")

#q5    
l1 = ["adnan" ,"xyz" , "jqz"]

name = input("Enter your name: ")

if(name in l1):
    print("Your name is present!")
else:
    print("Your name is not present!")    

#q6

a = int(input("Enter your marks: "))

if(a<=100 and a>=90):
    print("excelent",a)
elif(a<=90 and a>=80):
    print("A",a)
elif(a<=80 and a>=70):
    print("B",a)
elif(a<=70 and a>=60):
    print("C",a)
elif(a<=60 and a>=50):
    print("D",a)
else:
    print("fail")    