# define a function that take list of strings
# list containing reverse of every string 


# NOTE - USE LIST COMPREHENSION 
# and by using normal method 

# EX 
# l = ['abc', 'tuv', 'xyz']
# reverse_string(l) = ['cba', 'vut', 'zyx']

# l = ['abc', 'tuv', 'xyz']

# def reverse_string (a):
#     reverse_string = []
#     for i in a:
#         reverse_string.append(i[::-1])
#     return reverse_string

# print(reverse_string(l))

# BY LIST COMPREHENSION 
l = ['abc', 'tuv', 'xyz']
# reverse_string = [i[::-1] for i in l]
# print(reverse_string)
 
def reverse_list(a):
    # reverse_list = [i[::-1] for i in a]
    # return reverse_list
    return [i[::-1] for i in a]

print(reverse_list(l))