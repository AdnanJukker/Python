"""ARITHMETIC OPERATORS"""
"""
+ 	Addition 	x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	x / y 	
% 	Modulus 	x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division 	x // y
"""

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400) 
print(sum1,sum2,sum3)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

"""ASSIGNMENT OPERATORS"""

"""
= 	x = 5   x = 5 	
+= 	x += 3 	x = x + 3 	
-= 	x -= 3 	x = x - 3 	
*= 	x *= 3 	x = x * 3 	
/= 	x /= 3 	x = x / 3 	
%= 	x %= 3 	x = x % 3 	
//= 	x //= 3 	x = x // 3 	
**= 	x **= 3 	x = x ** 3 	
&= 	x &= 3 	x = x & 3 	
|= 	x |= 3 	x = x | 3 	
^= 	x ^= 3 	x = x ^ 3 	
>>= 	x >>= 3 	x = x >> 3 	
<<= 	x <<= 3 	x = x << 3 	
:= 	print(x := 3) 	x = 3 
print(x)
"""

"""COMPARISON OPERATORS"""

"""
== 	Equal 	x == y 	
!= 	Not equal 	x != y 	
> 	Greater than 	x > y 	
< 	Less than 	x < y 	
>= 	Greater than or equal to 	x >= y 	
<= 	Less than or equal to 	x <= y
"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)   

"""LOGICAL OPERATORS"""

"""
and  	Returns True if both statements are true 	x < 5 and  x < 10 	
or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
"""

"""IDENTITY OPERATORS"""

"""
is  	Returns True if both variables are the same object 	x is y 	
is not 	Returns True if both variables are not the same object 	x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

"""MEMBERSHIP OPERATORS"""

"""
in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y
"""

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

"""BITWISE OPERATORS"""

"""
&  	AND 	Sets each bit to 1 if both bits are 1 	x & y 	
| 	OR 	Sets each bit to 1 if one of two bits is 1 	x | y 	
^ 	XOR 	Sets each bit to 1 if only one of two bits is 1 	x ^ y 	
~ 	NOT 	Inverts all the bits 	~x 	
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2 	
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2
"""

print(6 & 3) 
print(6 | 3)
print(6 ^ 3)

"""OPERATOR PRECEDENCE"""

"""ORDER WISE"""

"""
() 	Parentheses 	
** 	Exponentiation 	
+x  -x  ~x 	Unary plus, unary minus, and bitwise NOT 	
*  /  //  % 	Multiplication, division, floor division, and modulus 	
+  - 	Addition and subtraction 	
<<  >> 	Bitwise left and right shifts 	
& 	Bitwise AND 	
^ 	Bitwise XOR 	
| 	Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
not 	Logical NOT 	
and 	AND 	
or 	OR
"""

print((6 + 3) - (6 + 3)) #Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first

print(100 + 5 * 3) #Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions

print(5 + 4 - 7 + 3) #Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right