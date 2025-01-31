# take two comma seperated inputs from user
# 1.User's Name
# 2.A Single Character
name,char = input("Type your name and Character seperated by comma:").split(",")


# Output two print lines
# 1. User's name lenght
# 2. count the character that user inputed (bonus; case insensitive count)
# print(len(name))
print(f"lenth of characters in your name is: {len(name)}")

# print(name.count(char.lower() and char.upper())) # wrong
# name.upper() ----> make all letter in name capital
# char.upper()---> make all letter in char capital
# print(name.upper().count(char.upper()))
print(f"Occurance of character input is : {name.upper().count(char.upper())}")

