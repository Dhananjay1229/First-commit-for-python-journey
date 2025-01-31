

# define a function for square of a number and then pass a list to the function
''' map(function,iterables)'''
# map object is iterable i.e you can run a loop on it for one time --->convert to list for running loop more than once 


numbers = [1,2,3,4,5]


# Method 0
def square(numbers):
    return numbers**2

# Method 1 

# def square(x):
#     squares = []
#     for i in x:
#         squares.append(i**2)
#     print(squares)
# square(numbers)


# Method 2 
sq = [i**2 for i in numbers]
# print(sq)

# method 3 
sq2 = map(square,numbers) #--> will give a map object

# print(list(sq2))

# Method 4 


sq3 = list(map((lambda x:x**2),numbers))
# print(sq3)


# length of strings in the list

names = ['abc','abcd','abcde']

# Method 1 
# print(len(names))   # length of whole list

for i in names:
    print(len(i))

# Method 2
names2 = []
for i in names:
    names2.append(len(i))
# print(names2)

# Method 3 
names3 = [len(i) for i in names]
# print(names3)

# Method 4
names4 = list(map(lambda i:len(i),names))
# print(names4)

# method 5
names5 = map(len,names)
print(list(names5))









