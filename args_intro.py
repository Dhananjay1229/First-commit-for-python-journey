# here we will study about the '*' argument

# example - we have to make a function to add two numbers 

def add (a,b):
    return a+b
# print(add(1,2))

# but if we want to add more than two numbers in same function 
# print(add(1,2,3)) # takes 2 positional arguments but 3 were given

# METHOD 1 WITH '*' ARGUMENT
def total (*args):      # we can use anything after '*' i.e *nums/*no etc
    total = 0           # it will make an tuple of passing arguments
    for i in args:
        total += i
    return total
print(total(1,2,3))

# METHOD 2 (BY TAKING AN INPUT FROM USER)

random = int(input("type how many numbers:"))

numbers = []
for i in range(1,random+1):
    numbers.append(i)
# print(numbers)

def all_total(l):
    total = 0
    for i in numbers:
        total += i
    return total

# print(all_total(numbers))
