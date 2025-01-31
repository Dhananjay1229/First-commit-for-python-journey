# numbers = list(range(1,11))

# def even (a):
#     even_numbers = []
#     odd_numbers = []
#     for i in a:
#         if i%2 == 0:
#             even_numbers.append(i)
#         else:
#             odd_numbers.append(i)
#     return even_numbers,odd_numbers

# # print(even(numbers))
# print(f"even numbers are {even(numbers)[0]} \nOdd numbers are {even(numbers)[1]}")

# BY USING LIST COMPREHENSION 

# def even(a):
#     even_num = [i for i in a if i%2 == 0 ]
#     odd_num =  [i for i in a if i%2 != 0]
#     return even_num,odd_num
# print(even(numbers))






# odd_numbers = [i for i in range(1,11) if i%2 != 0]
# print(odd_numbers)


# # another alternate in single line of code 
even = [ i for i in range(1,11) if i%2 == 0]
odd =  [ i for i in range(1,11) if i%2 != 0]
print(even)
print(odd)


