# class twoDvector:
#     def __init__(self, i ,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"i component is {self.i} and j component is {self.j}")

# class threeDvector(twoDvector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"i component is {self.i} and j component is {self.j} and k component is {self.k}")


# a = twoDvector(2, 3)
# a.show()
# b = threeDvector(4, 5, 6)
# b.show()        

# class animals:
#     pass
# class pets(animals):
#     pass
# class dogs(pets):
#     @staticmethod
#     def bark():
#         print("Woof!")

# d = dogs()
# d.bark()

# class employee:
#     salary = 10000
#     increment = 20
#     @property
#     def totalSalary(self):
#         return self.salary + (self.salary * self.increment / 100)   
    
#     @totalSalary.setter
#     def totalSalary(self, salary):
#         self.increment = ((salary - self.salary) / self.salary) * 100

# e = employee()
# print(e.totalSalary)
# e.totalSalary = 12000
# print(e.increment)         

# class complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i
#     def __add__(self, c2):
#         return complex(self.r + c2.r, self.i + c2.i)
#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c1 = complex(2, 3)
# c2 = complex(4, 5)
# print(c1 + c2)          


# class vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __add__(self, other):
#         return vector(self.i + other.i, self.j + other.j, self.k + other.k)
#         return result
    
#     def __mul__(self, other):
#         return self.i * other.i + self.j * other.j + self.k * other.k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
# v1 = vector(2, 3, 4)
# v2 = vector(4, 5, 6)
# v3 = vector(1, 2, 3)
# print(v1 + v2)
# print(v1 * v2)  
# print(v1 + v3)
# print(v1 * v3)

class vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = vector([1,2,3])
print(len(v1))