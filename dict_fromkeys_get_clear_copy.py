# fromkeys keyword

# if we want to make a dictionary like 
# user_info = {'name':'unknown','age':'unknown'} # same value for all the keys 
# we don't fill the value manually
# instead we use 

# user_info = dict.fromkeys(['name','age'],'unknown')
# print(user_info)

# .get() method 
user_info = {'name':'unknown','age':'unknown'}
# print(user_info['names'])       # for these type of error handling where we don't have
                                # a key asked in our dictionary and have to find its value 
# print(user_info.get('names'))       # it will show none instead of an error 

# if 'names' in user_info:
#     print('name is present')
# else:
#     print('name is absent')
#ANOTHER METHOD TO THIS IS if none-->false
# if user_info.get('names'):
#     print('present')
# else:
#     print('absent')

# clear will delete all inside our dictionary 
# user_info.clear()
# print(user_info)

# copy method will copy all of the data from our list to a new or existing list
# user_info2 = {}
# user_info2 =  user_info.copy()      # it will make a new dictionary 
# print(user_info2)

# print(user_info2 is user_info)  # false --> it makes a new dictionary with user_info2 == user_info as true with same values

user_info2 = user_info
print(user_info2)
print(user_info2 is user_info)      # cause it takes same memory location as user_info TRUE
