# we use in keyword with if statement for searching any specific character in the given string

name = "Dhananjay"
char = input("Enter any alphabet: ")

if char in name:
    print( f" '{char}' is present in the string")
    print(name.find(char))

else:
    print("False")