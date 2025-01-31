# define a function which will take a list as an input 
# and will give how many lists a list contains inside of it 
# ex. input [1,2,3,[1,2],[3,4]]-->output 2 



# brackets = [[6,6],1,2,3,[1,2],[3,4],[1,2]]
# def extractor (l):
#     lists = []          # it is always outside of the loop or it will update previous entries 
#     for i in l:         
#         if type(i) is list:
#             lists.append(i)
#         else:
#             continue
#     return lists

# print(extractor(brackets))

# def sublist_count (l):
#     count = 0
#     for i in l:
#         if type(i) is list:
#             count += 1
#     return count
# print(sublist_count(extractor(brackets)))


brackets = [[6,6],1,2,3,[1,2],[3,4],[1,2]]

def sub_list (l):
    i = 0
    count = 0
    sub_list = []
    while i < len(l):
        if type(l[i]) is list:
            count += 1
            sub_list.append(l[i])
        i += 1
    return f"You have {count} brackets and those are {sub_list}"

print(sub_list(brackets))





# def sub_list (l):
#     count = 0
#     i = 0
#     while i < len(l):
#         if type(brackets[i]) == list:
#             count += 1
#             i += 1
#         else:
#             continue
#     return count

# print(sub_list(brackets))            












# if type(brackets) is list:
#     print("your object is a list")

# if type(brackets2) is list:
#     print("yoyr object is a list")
# else:
#     print("your object is not a list")










# number1 = 1
# number2 = 2 

# def sum (a,b):
#     return a + b
# print(sum(number1,number2))