# define a function 
# input 
# num, iterable(tuple, list) containing numbers as args

# example 
# nums = [1,2,3]
# to_power(3,*nums)

# o/p
# list--->[1**3,8,27]

# if user didn't pass any args then give user a message 'hey you didn't pass any args'
# NOTE here we use if args: which can check args has any value in it or not 
# else 
# return list

# NOTE use list comprehension 

# def to_power (num,*args):
    
#     if args:                        # we check args has anything or not
#         to_power = []                     
#         for i in args:
#             to_power.append(i**num)
#         return to_power
#     else:
#         return "hey you didn't pass any args"
    

# l = [1,2,3]
# print(to_power(3))


def to_power (num,*args):
    if args:                            # it will check if the variable has a value or not  
        return [i**num for i in args]
    else:
        return "hey you didn't pass any args"

l = [1,2,3,4]
print(to_power(3,*l))




