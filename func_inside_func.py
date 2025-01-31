# define a function which takes three numbers as an input and return greater of the three numbers 

def greater_num(a,b):
    if a > b:
        return a
    else:
        return b

# def greatest(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c

def greatest(a,b,c):
    return (greater_num(greater_num(a,b),c))

print(greatest(100,2000,30))
