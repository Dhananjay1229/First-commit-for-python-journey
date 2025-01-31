# make odd number negative and square of even number

number = [-i if (i%2 != 0) else i**2 for i in range(1,11)  ] # if ,else put for statement in last 
print(number)

# for if else the output has to be different 

# numbers = list(range(1,11))
# # print(numbers)

# def new_nums(l):
#     new_nums = []
#     for i in l:
#         if i%2 != 0:
#           new_nums.append(-i)
#         else:
#             new_nums.append(i**2)
#     return new_nums
# print(new_nums(numbers))