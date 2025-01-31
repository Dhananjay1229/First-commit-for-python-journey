# .replace()
# .find()

string = "She is beutiful and she is a good dancer too"
print(string.replace("is","was"))
print(string.replace("is", "was", 1)) # 1-->how many "is" you want to replace

# print(string.find("is")) #----> 4
# print(string.find("is", 5))#--->24

# what if we don't know where the first "is" is and we have to know the position of second "is" ??
print(string.find("is", string.find("is") + 1))

