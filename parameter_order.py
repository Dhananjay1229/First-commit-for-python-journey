# PADK

# parameter
# *args
# default argument 
# **kwargs

def func(name,*args,last_name='Unknown',**kwargs):
    print(name)
    print(type(name))
    print(args)
    print(type(args))
    print(last_name)
    print(type(last_name))
    print(kwargs)
    print(type(kwargs))

func("Dhananjay",1,2,3,first_name ="Dhananjay",age = 30)