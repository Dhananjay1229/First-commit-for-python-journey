# common element finder function
# define a function which takes 2 lines as input and return a list 
# which contains common elements of both lines 

# example
# input [1,2,5,8] [1,2,7,6]--->output [1,2]

# #method 1
list1 = [1,2,5,8,7,123,3,100,21,3000]
list2 = [1,2,7,6,5,8,3000,10,121]

def common_element_finder (a,b):
    common = []
    for i in a:
        for k in range(len(b)): # k starts from 0 to the length -1
            if i == b[k]:
                common.append(b[k])
            else:
                continue
    return common

print(common_element_finder(list1,list2))


# # method 2
# list1 = [1,2,5,8]
# list2 = [1,2,7,6,5]

# def common_element_finder (a,b):
#     common = []
#     for i in a:
#         if i in b:
#             common.append(i)
#     return common
# print(common_element_finder(list1,list2))









