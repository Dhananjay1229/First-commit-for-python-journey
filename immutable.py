# strings in python are immutable 

string = "string"
# print(string.replace("t","T")) # "sTring-->it doesn't replace the character instead it make a new string
# print(string)  # ----> "string"

new_string = string.replace("t","T")
print(new_string)
print(string)

