name = "Dhananjay Chopade"

# 1.len() function -->measure length of string # also measures spaces in between
length = len(name)
print(f"Length of string is: {length}")

# 2. lower() method --> all characters in the string lower case
lower = name.lower()#---> in methods we use . before the method
print(f"All letters in Lower Case: {lower}")
# print(lower)
# print(name.lower())

#3. upper() method 
upper = name.upper()
print(f"All letters in Upper case: {upper}")

# 4. count() method ----> How many times a specific character appear
count = name.count("a")
print(f"Total \"a\" Characters in the string are: {count}")

# 5. title()
print(name.title())