# strings are immutable 
# lists are mutable 

s = "string"
t = s.title()
print(t)        # it doesn't change our original string # the changes are just temporary
print(s)        # strings are immutable # unchangeable

fruits = ['mango','orange','papaya','watermelon','cheeku', 'apple','mango']
fruits.pop()        # it results in deleting values of our lists permanantly
print(fruits)       # lists are mutable
fruits.append('kiwi')
print(fruits)


