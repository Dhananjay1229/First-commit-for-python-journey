# .get() method helps us in error handling
# this means if any value is not in our data or dictionary 
# we can bypass the error resulting in getting at least something as an output
# e.g. if we use 
user_info = dict(name = 'Dhananjay',age= 30,
    fav_movies= ['godfather','interstellar'],
    fav_songs= ['sunflower','heathens']
    )

# print(user_info['fav_movies'])  # it will surely print us an output cause the dict has that key available 
# but if we
# print(user_info['fav_places'])  # we got a key error 
# so we use 
print(user_info.get('fav_scenes')) 
print('fav_scenes', 'key not available')