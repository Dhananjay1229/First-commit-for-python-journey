# '**' argument
# it will interpret the provided arguments in the form of dictionary 

def func(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")
        


func(first_name = "Dhananjay", last_name = "Chopade")