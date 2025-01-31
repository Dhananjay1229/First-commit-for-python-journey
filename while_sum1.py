# exercise one of three
# sum of n natural numbers
# ask a user for natural number (n)
# print total from 1 to n

total = 0
i = 1
n = int(input("Type any number: "))
while i <= n:
    total = total + i
    i += 1      # i = i + 1
print(total)

