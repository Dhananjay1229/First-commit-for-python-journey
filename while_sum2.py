# problem
# ask user to input a number containing more than one digit 
# example - 1256
# calculate 1+2+5+6 and print

num = input("Enter number: ")
# print(int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
# print(len(num))

total = 0
i = 0
while i <= len(num) - 1:
    total = total + int(num[i])
    i += 1
print(total)







# algorithm - (method to solve problem in human language)
# ask input in string i.e. don't change string to integer 
# example- "1256"
# pick string character one by one and change to int 
# int(example[0]) + int(example[1]) + .............go upto len(example) - 1