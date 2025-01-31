# if elif else statement
# use for introducing multiple conditions 

# take input from user
age = int(input("Enter your age: "))
# print(type(age))
 
# show ticket pricing
# 0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

if age==0 or age<0:
    print("Please Enter valid Age")
elif 0 < age <= 3:
    print("Ticket Pricing: Free")
elif 4 <= age <=10:
    print("Ticket Pricing: 150")
elif 11 <= age <= 60:
    print("Ticket Pricing: 200")
else:
    print("Ticket Pricing: 250")
