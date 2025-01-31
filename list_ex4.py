# filter odd even 
# define a function 
# input [1,2,3,4,5,6,7]--->output[[1,3,5,7],[2,4,6]]

numbers =[1,2,3,4,5,6,7]

def odd_even (a):
    odd_numbers = []
    even_numbers = []
    for i in numbers:
        if i%2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return odd_numbers, even_numbers

print(odd_even(numbers))