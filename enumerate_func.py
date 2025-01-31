
# enumerate(l)=>> pos{0} name{abc}


l = ["abc","def","efg"]
# print(l)
# print(len(l))
# print(l[0])

#o/p 0-->abc,1-->def
# Method 1 (for loop with item)
# pos = 0
# for i in l:
#     print(pos,i)
#     pos +=1

# Method 2(for loop with range)
# for i in range(0,len(l)):
#     print(i,l[i])

# Method 3(while loop)
# i = 0
# while i<len(l):
#     print(i,l[i])
#     i += 1

# Method 4(list comprehension)
# l = ["abc","def","efg"]
# for i in range(0,len(l)):
        # print (i)

# pos_cont = [i for i in range(0,len(l))] # [0, 1, 2]

# def pos(a):             #taking input from another function 
#     for i in pos_cont:
#         print (i,a[i])
# pos(l)                  # calling the final function 

# Method 5 (By using enumerator func)
l = ["abc","def","efg"]
# for pos,name in enumerate(l):       #enumerate(l)=>> pos{0} name{abc}
    # print(f"{pos}---{name}")




# exercise
l = ["abc","def","efg"]
# print(l.index("efg"))
# word = input("Type a word: ")

def find_pos(x,input):
    for pos,name in enumerate(x):
        if input in name:
            return pos
    return -1
print(find_pos(l,"efg"))
        