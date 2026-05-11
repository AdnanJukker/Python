import random
n = random.randint(1, 100)
guess = 1
a = -1
while a != n:
    a = int(input("Enter your guess: "))
    if a < n:
        print("Too low! Try again.")
    elif a > n:
        print("Too high! Try again.")
    guess +=1
    
print(f"Congratulations! You've guessed the number {n} in {guess} attempts.")