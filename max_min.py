numbers = [6,60,2]
# print(min(numbers))
# print(max(numbers))

# define a function which will take an input as a list 
# will give greatest difference i.e max-min as an output

def greatest_diff (l):
    greatest_diff = max(l)-min(l)
    return greatest_diff

print(greatest_diff(numbers))