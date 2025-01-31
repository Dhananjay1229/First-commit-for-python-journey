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



# name = input("Enter a name: ")
# i = 0
# temp_var = ""

# while i < len(name) :
#     if name[i] not in temp_var:
#         # temp_var = name[i] # it will result in replacing the value every time not storing it 
#         temp_var += name[i]
#         print(name[i],":",name.count(name[i]))   
#     i += 1


# print(name[2],":", name.count(name[2]))



v = "Dhananjay"
t =""
for i in v:
    if i not in t:
        print(i,v.count(i))
        t += i
# print(v[0],v.count(v[0]))