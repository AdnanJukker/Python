tsisList = ["one","two","three"]
print(tsisList)

"""LIST LENGTH"""

print(len(tsisList))

"""ACCESS ITEMS"""
print(tsisList[1])

"""NEGATIVE INDEXING"""
print(tsisList[-1])

"""RANGE INDEXING"""
print(tsisList[1:3])

"""check if items present"""
if "two" in tsisList:
    print("YES there is two")

"""CHANGE LIST ITEM """
tsisList[1] ="four"
print(tsisList)

"""APPEND ITEM IN LIST"""
tsisList.append("two")
print(tsisList)

"""INSERT ITEM IN LIST"""
tsisList.insert(2,"six")
print(tsisList)

"""EXTEND LIST"""
fruitList = ["apple","mango","tomato"]
tsisList.extend(fruitList)
print(tsisList)

"""REMOVE ITEM"""
tsisList.remove("two")
print(tsisList)

tsisList.pop(2)
print(tsisList)

del tsisList[4]
print(tsisList)

tsisList.clear()
print(tsisList)

tsisList = ["one","two","three"]

"""LOOP THROUGH LIST"""

for x in tsisList:
    print(x)

for i in range(len(tsisList)):
    print(tsisList[i])    

i=0
while i< len(tsisList):
    print(tsisList[i]) 
    i = i+1

[print(x) for x in tsisList]

newlst = []
for x in tsisList:
    if "o" in x:
        newlst.append(x)

print(newlst)    

newlst = [x for x in tsisList if "o" in x]
print(newlst)

#newlist = [expression for item in iterable if condition == True]
newlst = [x for x in tsisList if x != "one"]
print(newlst)

newlst = [x for x in range(10)]
print(newlst)

newlst = [ x for x in range(10) if x < 5 ]
print(newlst)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

"""METHODS"""

"""
append()	Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""