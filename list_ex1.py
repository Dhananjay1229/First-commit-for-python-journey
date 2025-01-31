# define a function which will take list containing number as an input 
# and return list containing add of every elements 

# numbers = [1,2,3,4]
# num = int(input("How many numbers from 1 you want adds: "))
# numbers = list(range(1,num+1))

# def add_list (a):
#     add_list = []
#     for i in range(1,len(a)+1):
#         add_list.append(i**2)
#     return add_list

# print(add_list(numbers))


# numbers = [1,2,3,4]

# def add_list (a):
#     add_list = []
#     for i in numbers:       # here i will start to pick character from 0th position by default
#         add_list.append(i**2)
#     return add_list

# print(add_list(numbers))

# numbers = [1,2,3,4]

# def add_list (a):
#     add_list = []
#     i = 0
#     while i < len(numbers):
#         add_list.append(numbers[i]**3)
#         i += 1
#     return add_list

# print(add_list(numbers))

numbers = [1,2,3,4]

def add(a):
    total = 0
    for i in numbers:
        total += i
    return total
print(add(numbers))
        




# name = "Dhananjay"
# for i in name:
#     print(i)

# i = 0
# while i <= len(name)-1:
#     print(name[i])
#     i += 1


