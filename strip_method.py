# for removal of unwanted spaces in our variables
# we use .strip() function

name = "   Dhananjay    "
dot ="....."
print(name + dot)

# for removal of user input spaces from left
# print(name.lstrip() + dot)

# for removal of user input spaces from right
# print(name.rstrip() + dot)

# for removal of user input spaces anywhere
# print(name.strip() + dot)


# we can also use .replace function for removal of spaces
# print(name.replace(" ","") + dot)


# take two comma separated inputs from user
# 1.User's Name
# 2.A Single Character
name,char =input("Type your name and char separated by comma: ").split(",")
# Output two print lines
# 1. User's name length
# "  DhAnanjay" ---->"DhAnanjay"---->"dhananjay"
print(f"Total characters in your name are: {len(name.strip().lower())}")
# 2. count the character that user inputted in name  (bonus; case insensitive count)
# " A"---->"A"----->"a"
# (char.strip().lower())
print(f"Given Character Repeated: {name.lower().count(char.strip().lower())}")


