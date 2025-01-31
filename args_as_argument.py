# NOTE *args as an argument will unpack all elements from given input i.e list,tuple etc

def mul (*args):            # here it is as parameter 
    multiplication = 1
    for i in args:
        multiplication *= i
    return multiplication

l = (2,3,3)
# l = {2,3,3} NOTE for this it will show 2*3 only coz set not take repetition 
# print(mul(l))   # here it will take whole list as a single argument
print(mul(*l))             # here we take it as an argument

print(type(l))