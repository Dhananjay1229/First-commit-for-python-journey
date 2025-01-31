# Exercise - Watch COCO
# Ask User's name and age 
name, age = input("Type your name and age by comma seperated: ").split(",")

# name = input("Enter your name: ")
# age = int(input("Enter your Age: "))
# print(name[0])

# age = int(input("Enter your age: "))

# if user's name starts with ('a' or 'A') and age is above 10 then
if (name.strip()[0] == "A" or name.strip()[0] == "a") and int(age) >= 10:
# print 'you can watch COCO movie'
    print("You can watch COCO movie")
# Else print 'Sorry, you cannot watch COCO'
else:
    print('Sorry, you cannot watch COCO')
   


