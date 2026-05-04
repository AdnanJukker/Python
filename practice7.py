#qq1
i = 1
while (i<51):
    print(i)
    i += 1

#qq2
l= ["A","abc","abcd",False,"abcde"]
i=0
while (i<len(l)):
    print(l[i])
    i+=1
#q1
a = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{a}x{i}={a*i}")

#q2
l = ["adnan","sohan","rahul","sachin"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")
#q3
a = int(input("Enter the number: "))
i = 1
while (i<11):
    print(f"{a}x{i}={a*i}")
    i += 1

#q4
n = int(input("Enter the number: "))
for i in range(2,n):
    if (n%i) == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is prime number")    

#q5
a = int(input("Enter the number: "))
total_sum=0
i=1
while i<=a:
    total_sum+=i
    i+=1
print(f"the sum of first {a} number is {total_sum}")    

#q6

a = int(input("Enter the number: "))
product = 1
for i in range(1,a+1):
    product = product*i
print(f"the factorial of {a} is {product}")

#q7
n =int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-1),end="")
    print("*"* (2*i-1),end="")
    print("")

#q8
n =int(input("Enter the number: "))
for i in range(1,n+1):
    print("*"* i,end="")
    print("")

#q9
n =int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")    
        print(" "*(n-2),end="")    
        print("*",end="")
    print("")        
        
#q10
n =int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")