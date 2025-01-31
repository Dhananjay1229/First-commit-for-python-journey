x = 5           # here x = 5 is global variable
def func():
    global x    # it changes the global variable value i.e x becomes 7
    x = 7       # here x = 7 is local variable
    return x

print(x)        # it prints global variable firstly because it doesn't change firstly
print(func())   # it changes our global variable to x = 7
print(x)        # our global variable changed because of the defined function 



