try:
    with open("file1.txt") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open("file2.txt") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")   
try:
    with open("file3.txt") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")        

l = [1,2,3,4,5,6,7,8,9,10]

for i,item in enumerate(l):
    if i == 2 or i ==4 or i ==6:
        print(f"index: {i} value: {item}")

n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
print(table)
with open("table.txt","w") as f:
        f.write(f"Table of {n}: {str(table)}\n")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinit")