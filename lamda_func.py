# lambda function    
# anonymous function --> this function has no name, normal function has name stored 
''' lambda arguments:o/p'''

'''addition function with traditional methods of arguments'''

def add(*args):
    total = 0
    for i in args:
        total += i
    return total

l = list(range(0,10))
# print(add(*l))

'''addition function using lambda'''

add2 = lambda x,y: x+y
# print(add2(5,10))

# print(add)
# print(add2)


"""Lambda Function with if else"""
# Method 1 
is_greater = lambda s : True if len(s)>5 else False # no need fpr return # expected result and condition
# print()
# print(f'Your string consist of more than 5 words: {is_greater("Dhananjay")}')      # we cannot " "_" "

is_greater2 = lambda s: len(s)>5
# print(is_greater("D"))























add_15 = lambda x: x+15
# print(add_15(2))



welcome = lambda s: print(f"Welcome {s}")
# print(welcome("Dhananjay"))


numbers = ["a","b","c","d"]
# print(numbers)

# for i in numbers:
    # print(i,numbers.index(i))

pos = [(f"alphabet:{i}, at position:{numbers.index(i)}") for i in numbers ]
# print(pos)

