# centre method 
# it can centered our string around a given character input 

name = "Dhananjay"
name.center(11,"*") #-----> our character lenght 9 + how many characters arount it we want
print(name.center(11,"*"))

# The fill character must be exactly one character long
# we dont know how much the lenght of string from user input

name = input("Type your name: ")
len(name) + 26, "$"
name.center(len(name) + 26, "$")
print(name.center(len(name) + 26, "$"))