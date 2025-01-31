# PADK
# parameter,args,default parameter,kwargs(keyword arguments)

'''addition function with parameters'''
#limited number of arguments 
def add(x,y):
    return x + y
# print(add(5,4))

'''addition function with default arguments '''
# we have set the value of arguments 
def add(a = 5,b=5):
    return a + b
# print(add())

'''addition function with *args'''
# used for taking multiple arguments inside a function 
def add(*args):     #it will take the argument inside a tuple and return a tuple 
    total = 0
    for i in args:
        total += i
    return total
t = (1,2,3)
# print(add(t)) ## it wil take a tuple inside a tuple of the *args function creating an error 
# this * will unpack out tuple print(t)-->(1,2,3) & print(*t)--> 1 2 3 
# print(add(*t))

'''function with **kwargs'''
# Taking its arguments as a dictionary
def func(**kwargs):
    return kwargs
# print(func(Name="Nikhil",Age=28))

# # data = dict(Name="Dhananjay",Age=29)
# data ={"Name":"Shivam","Age":28}
# print(data)


# all together 
# PADK

def all_together(x,y,*args,Default_Name="Shivam",**kwargs):
    print(x,y)
    print(args)
    print(Default_Name)
    print(kwargs)

all_together(1,2,1,2,3,Name="Dhananjay")
    
    

