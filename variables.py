x = 5 #x is of type int
y= "Adnan" # y is of type str
print(x)
print(y)

a = str(3) #a will be '3'
b= int(3) # b will be 3
c = float(3) #c will be 3,0

d = 5
e = "Adnan"
print(type(d))
print(type(e))

f,g,h = "banana","orange","melon" #many values to multiple variables
print(f,g,h)

i = j = k = "Apple" #one value to multiple variables
print(i,j,k)

#unpack collection
fruits = ["apple", "banana", "orange"]
x, y, z = fruits
print(x,y,z) 

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("python is" + x)    