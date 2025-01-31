# ask user a number like 1256
# calculate sum of digits-----> 1+2+5+6

# by using while loop
# num = input("Enter a number: ") # "1256"
# i = 0
# total = 0
# # num[i]
# while i <= len(num) - 1:
#     total += int(num[i])
#     i += 1
# print(total)

num = input("Enter a number: ")
# print(num[0])
# print(len(num))
total = 0
for i in range (0, len(num)):
    total += int(num[i])
print(total)






