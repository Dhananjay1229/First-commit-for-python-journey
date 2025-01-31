# update a dictionary 
# if we try to update a dictionary with the same key it will overwrite the value of that key

# making a dictionary 
user_info = dict(name = 'Dhananjay',age= 30,
    fav_movies= ['godfather','interstellar'],
    fav_songs= ['sunflower','heathens']
    )
# print(user_info)

more_info = {
    'fav_place' : ('shimla','manali'),   # saved as tuple
    'fav_sport' : 'f1' 
}

# print(more_info)
# print(type(more_info['fav_place']))


user_info.update(more_info)

print(user_info)

