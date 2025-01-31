# we can use in operator to find any keys/values from the dictionary 
# by default the in operator shows us the keys 
# but for values and items we have to use .values() and .items() methods 
# in looping if only calls for i in given dictionary by default those i's are keys 




user = {
    'name' : 'Dhananjay',
    'age': 30,
    'hobbies': 'watching movies,series',
    'fav_movies':['godfather','interstellar'],
    'fav_songs':['sunflower','heathens']
}
# print(user)


# we can use in operator to find any keys/values from the dictionary 
# if 'fav_actors' in user:
#     print("present")
# else:
#     print("not present") 

# but for values and items we have to use .values() and .items() methods 
# if 30 in user.values():
#     print('present')
# else:
#     print('not present')

## VALUES METHOD 
# user_values = user.values()
# print(user_values)        # results in a list of values 
# print(type(user_values))  # but we cannot add,delete data like list but only iterate 

# for loop
# for i in user:      # by default the i's are taken for keys 
#     print(i)

# for i in user.values(): # by .values() method we can take values in consideration 
#     print(i)
# OR for same output
# for i in user:
#     print(user[i])      # user[i] fro accessing the values # in list we use users[0,1,2,etc] because that was ordered collection of data and there indexing is possible 

# ITEMS METHOD 
# it will generate a data in key and value pair 
# user_items = user.items()      # it will generate a data in key and value pair
# print(user_items)              # in a tuple like format
# print(type(user_items))

# for i in user.items():
#     print(i)        # it will generate a data in key and value pair in tuple like fromat

# we know tuple unpacking by giving exact number of values which are contained by our tuple
# names = 'Dhananjay','Shivam','Sanket','Nikhil'
# print(names)    # names saved inside a tuple ('Dhananjay', 'Shivam', 'Sanket', 'Nikhil')
# now for unpacking we have to give same number of values 
# name1,name2,name3,name4 = (names)
# print(name1)

# same concept for dictionary unpacking which has two values 1--> key, 2--> value

# for i,j in user.items():
#     print(f"your key is {i}, your value is {j}")