#q1
words = {
    "kaam" : "work",
    "madad": "help",
    "kursi" : "chair"
}

word = input("Enter the you want the meaning of :")
print(words[word])

s = set()
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
n = input("Enter the numbers : " )
s.add(int(n))
 
print(s)

#q2
s = {18,"18"}

print(type(s))

#q3
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

#q4
d = {}

name = input("Enter your names :  ")
lang = input("Enter your fav lang: ")
d.update({name:lang})
name = input("Enter your names :  ")
lang = input("Enter your fav lang: ")
d.update({name:lang})
name = input("Enter your names :  ")
lang = input("Enter your fav lang: ")
d.update({name:lang})
name = input("Enter your names :  ")
lang = input("Enter your fav lang: ")
d.update({name:lang})

print(d)