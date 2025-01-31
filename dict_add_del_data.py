# add data in a dictionary ###key and value 
# delete data in a dictionary # pop and pop.item methon 

user_info = {
    'name':'Dhananjay',
    'age': 30,
    'fav_movies':['godfather','interstellar'],
    'fav_songs':['sunflower','heathens']
}



# add data in a dictionary
## user_info = dict(hobbies = 'watching movies')   # it will replace the value of our existing dictionary 
user_info['hobbies'] = ('watching movies,series')
# print(user_info)
##print(type(user_info['hobbies'])) # although is is inserted as a tuple but its type is string cause tuple saves in the key,value format 


# delete data in a dictionary
# method 1
# user_info.pop('age') # it will pop key but store its value 
# popped_value = user_info.pop('age')
# print(type(popped_value))
# print(popped_value)
# print(user_info)


# method 2
# user_info.popitem()
popped_item = user_info.popitem()       # it will delete last key:value from the list  
print(type(popped_item))                # and save it as a tuple 






