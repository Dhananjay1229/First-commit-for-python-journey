# name = "Dhananjay"
# print(len(name))    #len is a function predefined 

# Define a functions # we can make our own functions 
def add_two(a,b):
    return a+b

# # total = add_two(5,4)
# # print(total)
# print(add_two(5,3))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(add_two(num1,num2))

# We can also concat two strings by using functions 
# because python is a dynamically typed language 
# dynamically typed language --> it means no need to type data type while assigning value to variable
# for num = "Dhananjay" 
# it can take anything as variable value without defining its data type

first_name,last_name = input("Type first name & last name :").split(",")
print(add_two(first_name,last_name))
