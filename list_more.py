# generate list with range function 
# numbers = list(range(1,11))
# print(numbers) 

# more about .pop() method
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(numbers)
# # numbers.pop()
# # print(numbers)
# # popped_num = numbers.pop()
# print(numbers.pop())
# print(numbers)

# index method 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,2]
# print(numbers.index(2,2))

# pass list to a function
# make a function which gives a negative list of provided list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_list (a):
    negative = []
    for i in a:
        negative.append(-i)
    return negative

print(negative_list(numbers))






