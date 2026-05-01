a =20
b =33
if a > b:
    print("a is greater")
else:
    print("b is greater")

logged_in = True
if logged_in:
    print("Wrlcome Back!")

a = 40
b = 40
if b > a:
    print("b greater")
elif a == b:
    print("both are equal")


score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")


day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

a= 20
b = 40
print("A") if a > b else print("B")

bigger = a if a > b else b
print("bigger is", bigger)

a =330
b = 330
print ("A") if a > b else print("=") if a == b else print ("B") 

a = 330
b = 40
c = 330
if a > b and c > b:
   print("Both condition are true")
if a > b or c > b:
   print("Least one conditon should be true")

a = 33
b = 200
if not a > b:
   print("a is not greater than b")

age = 25
student = False
discount = True
if (age < 18 or age > 65) and not student or discount:
   print("discount applies")

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

a =30 
b =40
if b > a:
  pass      