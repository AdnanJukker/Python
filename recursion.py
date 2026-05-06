def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

user = int(input("Enter the number: "))
print(f"The factorial of {user} is {factorial(user)}")