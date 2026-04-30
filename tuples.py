"""A tuple is a collection which is ordered and unchangeable."""
mytuple = ("apple", "banana", "cherry")


""" Using Asterisk* """
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 

"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""