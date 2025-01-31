# define a function which will take list as an argument and this function 
# will return a reversed list 
# by using pop and append method

# # First method 
# number = [1,2,3,4]
# print(number[::-1])

# # second method 
# number = [1,2,3,4]
# number.reverse()
# print(number)

# third method with the help of pop and append
# number = [1,2,3,4]

# def reversed_list (a):
#     reversed_list = []
#     for i in range(1,len(a)+1):
#         popped_item = a.pop()
#         reversed_list.append( popped_item)
#     return reversed_list

# print(reversed_list(number))


# number = [1,2,3,4,5]
# wrong         # .pop will always changes our list permanently
# print(number)
# popped = number.pop()
# print(popped)
# def reverse_list (a):
#     reverse_list = []
#     for i in a:
#         popped = a.pop()            # [1,2,3,4][5] #[1,2,3][4,5] #[1,2][5,4,3]
#         reverse_list.append(popped)
#     return reverse_list

# print(reverse_list(number))


unsorted_list = [2,4,5,32,6,255,5,42]
unsorted_list.sort()
print("Now it is sorted:", unsorted_list)