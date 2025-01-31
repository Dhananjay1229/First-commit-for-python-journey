# make a func which decides whether the number is even or odd
# i/p "Enter a number:" o/p "True/False"


# Method 1 
# x = int(input("Enter a Number:"))
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
# print(f"Your Number is Even: {is_even(x)}")

# Method 2
# x = int(input("Enter a Number:"))
def is_even(x):
    return x%2 ==0      # True 
# print(f"Your Number is Even: {is_even(x)}")

# Method 3
# x = int(input("Enter a Number:"))
is_even = lambda x: x%2 ==0
# print(is_even(x))

# define a func which gives last char of a string
last_char = lambda x:x[-1]
# print(last_char("Dhananjay"))

"""Lambda Function with if else"""
# Method 1 
is_greater = lambda s : True if len(s)>5 else False # no need fpr return # expected result and condition
# print()
# print(f'Your string consist of more than 5 words: {is_greater("Dhananjay")}')      # we cannot " "_" "

is_greater2 = lambda s: len(s)>5
# print(is_greater("D"))

add_15 = lambda number : number + 15
# print(add_15(10))

mul = lambda x,y: x*y
# print(mul(2,5))








# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
add_15 = lambda a: a+15
# print(add_15(55))

mul = lambda x,y: x*y
# print(mul(3,3))

# Create a function that takes one argument multiplied with an unknown given number
number = int(input('How many times you want: '))
times_x = lambda x: x*number
# print(f"Double the number of 2 = {times_x(2)} ")




