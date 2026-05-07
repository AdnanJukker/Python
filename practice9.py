# f = open("poem.txt")
# c = f.read()
# if "twinkle" in c:
#     print("twinkle is present")
# else:
#     print("twinkle is not present")    
# f.close()
# import random

# def game():
#     print("You are playing the game")
#     score = random.randint(1, 62)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#     if (hiscore != ""):
#         hiscore = int(hiscore)
#     else:
#         hiscore = 0 

#     print(f"Your score is: {score}")
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()


# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n*i}\n"
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2, 21):
#     generateTable(i) 

# word = "donkey"

# with open("file.txt", "r") as f:
#     c = f.read()

#     contentNew = c.replace(word, "######")
# with open("file.txt", "w") as f:
#     f.write(contentNew)


# word = ["donkey","brainless","gande"]

# with open("file.txt", "r") as f:
#     c = f.read()

#     for w in word:
#         c = c.replace(w, "#"*len(w))

# with open("file.txt", "w") as f:
#     f.write(c)

# with open("log.txt", "r") as f:
#     c = f.read()
# if "python" in c:
#     print("python is present")
# else:    print("python is not present")

# with open("log.txt") as f:
#     lines = f.readlines()
# lineno = 1
# for line in lines:
#     if "python" in line:
#         print(f"python is present, line number is: {lineno}")
#         break
#     lineno += 1
# else:
#         print("python is not present")

# with open("file.txt") as f:
#     c =f.read()

# with open("copy_file.txt", "w") as f:
#     f.write(c)

with open("file1.txt") as f:
    c1 = f.read()
with open("poem.txt") as f:
    c2 = f.read()

if c1 == c2:
    print("Both files are same")
else:
    print("Both files are different")
