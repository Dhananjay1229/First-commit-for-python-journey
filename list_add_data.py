# By insert method
# How to join(concat) two lists 
# extend method 
# difference between append and extend method 

fruits1 = ['mango','orange']
# print(fruits1)
# fruits1.insert(1, 'banana')     # we can insert object at our desired position 
# print(fruits1)

fruits2 = ['papaya','watermelon']

# fruits = fruits1 + fruits2
# print(fruits)

fruits3 = ['cheeku', 'apple']

# fruits1.extend(fruits2)       # one at a time 
# fruits1.extend(fruits3)
# print(fruits1)

fruits1.append(fruits2)     # will print list inside a list
print(fruits1)

