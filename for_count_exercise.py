# ask the user for a name 
# Example - Dhananjay Chopade 
# print count of each word 
# Output:
        # D : 1
        # h : 2
        # a : 4
        # n : 2
        # j : 1
        # y : 1
        #   : 1
        # C : 1
        # o : 1
        # p : 1
        # d : 1
        # e : 1

name = input("Type your name: ")
my_storage_string = ""
for i in range (0, len(name)):
        if name[i] not in my_storage_string:
                my_storage_string += name[i]
                print(name[i],":",name.count(name[i]))