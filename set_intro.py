# unordered collection of UNIQUE data 
# we cannot store list and tuple in it 
# basically sets are used to remove repetition in list or dictionary

set_1 = {1,1.2,"Dhananjay",1.0} #o/p--> {1, 'Dhananjay', 1.2} unique and unordered collection of data 
print(set_1)

s = {1,2,3} # same as dict in notations but 
s = {1,2,2,1,3} # o/p--> {1, 2, 3} unique collection of data 

# add data in set
s.add(4)

# remove data 
s.remove(4)
# s.remove(5) # error , 5 not present in our set so for handling this kind of error 
s.discard(5)    # no remove no error 
# print(s)

l = [1,1,2,2,3,2,1,3,4,2,4,2,1] # repeated entries
# for fixing this 
s1 = set(l) # will remove repeated entries # unique data 
# print(s1)

# copy
s2 = s1.copy()
# print(s2)

#clear
s1.clear()
print(s1)



