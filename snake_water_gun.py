"""
snake = 1
water = -1
gun = 0
"""
import random
computer = random.choice([1, -1, 0])
youstring = input("Enter your choice (snake, water, gun): ")
youdict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}
you = youdict[youstring]

print(f"You chose {reverse_dict[you]} \n Computer chose {reverse_dict[computer]}")

if you == computer:
    print("It's a tie!")

else:
    if(you ==1 and computer == -1):
        print("You win!")
    elif(you == -1 and computer == 0):
        print("You win!")
    elif(you == 0 and computer == 1):
        print("You win!")
    elif(you == -1 and computer == 1):
        print("Computer wins!")
    elif(you == 0 and computer == -1):
        print("Computer wins!")
    elif(you == 1 and computer == 0):
        print("Computer wins!") 
    else:
        print("Invalid input! Please enter 's', 'w', or 'g'.")        