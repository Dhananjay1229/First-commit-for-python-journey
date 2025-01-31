# define a function which takes two numbers as an input and return greater of the two numbers 

def greater_num(a,b):
    if a > b:
        return a
    return b

num1,num2 = input("Enter first num & second num:").split(",")

print(f"Greater number is {greater_num(int(num1),int(num2))}")

