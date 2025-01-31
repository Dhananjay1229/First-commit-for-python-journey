# num to string
# define a function 


# example
# input ---> [True, False, [1,2,3], 1, 1.0, 3]
# output --> ['1', '1.0', '3']

list_1 = [True, False, [1,2,3], 1, 1.0, 3]
# for i in list_1:
#     print(i,type(i))

# def string_ex (a):
#     list_2 = []
#     for i in a:
#         if type(i) is int or type(i) is float:
#             list_2.append(str(i))
#     return list_2

# print(string_ex(list_1))


# alternate by list comprehension 
def string_ex(l):
    return [str(i) for i in l if type(i) is int or type(i) is float]
print(string_ex(list_1))