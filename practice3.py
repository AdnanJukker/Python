userName = input("Enter your Name:  ")
print(f"Good AfterNoon {userName}") 

letter = '''Dear <|Name|>
            You are selected !
            <|Date|>'''
print(letter.replace("<|Name|>","Adnan").replace("<|Date|>","23 March 2028"))

name = "your  name is Adnan  Jukker"
print(name.find(" "))
print(name.replace("  "," ")) 

letter = "Dear Adnan,\n This Python Course is nice.\n Thanks!"
print(letter)