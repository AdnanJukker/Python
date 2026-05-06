# qq1
def greet():
    print("Hello, welcome to the world of Python programming!")

greet()

# q1

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
print(f"The greatest number among {a}, {b} and {c} is {greatest(a,b,c)}")

# q2

def farenheit_to_celsius(f):
    return (f-32)*5/9
    
f = int(input("Enter the temperature in Fahrenheit: "))
c = farenheit_to_celsius(f)
print(f"The temperature in Celsius is {c:.2f}°C")

# q3
def sum_of_natural_numbers(n):
    return n*(n+1)//2
n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")

# q4
def pattern(n):
        if n == 0:
            return
        print("*" * n)
        pattern(n-1) 

n = int(input("Enter the number of rows: "))
pattern(n)

# q5
def inches_to_centimeters(n):
    return n * 2.54
inches = float(input("Enter the length in inches: "))
centimeters = inches_to_centimeters(inches)
print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")

# q6
def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
multiply(5)
