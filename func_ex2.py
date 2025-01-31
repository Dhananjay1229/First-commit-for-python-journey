# define a function which takes three numbers as an input and return greater of the three numbers 

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


print(f"{greatest(num1,num2,num3)} is the greatest number")