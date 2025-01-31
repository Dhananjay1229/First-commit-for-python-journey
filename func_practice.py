# define a function as a input taking one parameter name return its last character

# def last_char(name):
#     return(name[-1])

# name = input("Type your last name:")
# print(last_char(name.strip()))


# define a function for finding out a num is even or odd

# def even_odd(num):
#     if num%2 == 0:
#         return "Number is even"
#     # else:
#     #     return "Number is odd"
#     return "Number is odd"

# print(even_odd(8))

# define a function which tells our number is even or not by boolean output i.e true or false 

def is_even(num):
    if num%2 == 0:
        return True
    return False

print(is_even(90))

# OR

def is_even(num):
    return num%2 == 0

print(is_even(3))

# we can define a function without giving parameters 

def name():
    return "Dhananjay Chopade"

print(name())

