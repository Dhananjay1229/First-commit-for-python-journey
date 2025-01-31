# we use list comprehension to make a list with minimum line of code
# [desired o/p --loop--condition]

# make a list containing 1 to 10 numbers

# METHOD 1
# numbers = list(range(1,11))
# print(numbers)

# METHOD 2
# numbers = []
# for i in range(1,11):
#     numbers.append(i)
# print(numbers)

# METHOD 3
# number = [ i for i in range(1,21)]
# print(number)

# make a list containing squares of numbers between 1 to 11
# numbers = [1,2,3,4,5,6,7,8,9,10,11]
# squares = []
# for i in numbers:
#     squares.append(i**2)
# print(squares)

squares = [i**2 for i in range(1,11)]   # logic--> what we want first and then our loop
# print(squares)

# 
names = ['Dhananjay', 'Shivam', 'Aniket']
# initials = []
# for i in names:
#     initials.append(i[0])
# print(initials)

#alternate 
initials = [ i[0] for i in names]
print(initials)

