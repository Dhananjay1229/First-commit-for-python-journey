# o/p --> [[1,2,3],[1,2,3],[1,2,3]]

new_list = [[i for i in range(1,4)] for j in range(1,4)]
# print(new_list)



#o/p--> [[1,3,5,7,9],[2,4,6,8,10]]
even_odd = [[i for i in range(1,11) if i%2 != 0],[i for i in range(1,11) if i%2 == 0]]
# print(even_odd)


# alternate 
new_list2 = []
for j in range(1,4):
    new_list2.append([i for i in range(1,4)])
# print(new_list2)
