# we use break/continue statement for taking us outside the loop 

# break statement
# print 1,2,3,4,5,6,7,8,9,10 
# but I only want to print till 5
for i in range(1,11):
    if i == 5: # when i reaches to 5 it will discard the loop
        break
    print(i)

# continue statement
# print 1,2,3,4,5,6,7,8,9,10
# but i have to skip 5
for i in range (1,11):
    if i == 5: # when i reaches to 5 it will take us outside the loop and again the cycle repeats itself
        continue
    print(i)
