# arguments with parameters 
# NOTE WE CANNOT TAKE (*args, num) as this will load all values in args tuple as we can 
# have lack of num parameter 

def mul (num,*args):
    print(num, type(num))
    print(args, type(args))
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

# print(mul(2,3,3)) #----> # will take (2,3,3) as a tuple for  def mul (*args):
print(mul(2,3,3))   # it will take the first 2 as num parameter and (3,3) as a separate tuple 



