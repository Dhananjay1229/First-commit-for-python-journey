# LOOPS IN TUPLE --> just like a normal list function 
# LIST INSIDE A TUPLE 
# ADDING A SINGLE ELEMENT IN A TUPLE --> we have to introduce a comma 
# TUPLE UNPACKING--> assign number of variables == number of values inside the tuple 
# TUPLE WITHOUT PARENTHESIS



# LOOPS IN TUPLE
# mixed = (1,2,3,4.0)

# for i in mixed:
#     print(i)

# i = 0
# total = 0
# while i < len(mixed)+1:
#     total += i
#     i += 1
# print(total)

# LIST INSIDE A TUPLE 
# favorites = ('godfather','interstellar',['leonardo di caprio','christian bale',['sunflower','heathens']])
# favorites[2].append('keanu reeves')
# # print(favorites)
# favorites[2][2].append('calm down')
# favorites[2][2].insert(1,'hold my hand') # adding a data on a particular position 
# print(favorites)

# ADDING A SINGLE ELEMENT IN A TUPLE
# number = (1)  # by this it cannot add inside a tuple 
# print(number) # it adds just like a normal value assign to a variable 
# number =(1,)        # by adding a comma inside parenthesis we can make it a tuple 
# print(number)

# TUPLE UNPACKING
# fav_movies1,fav_movies2, fav_actors = (favorites)
# favorite_actors1,favorite_actor2,favorite_songs = (fav_actors)
# print(f"favorite movies are:{fav_movies1,fav_movies2}  \nfavorite actors are:{favorite_actors1,favorite_actor2} \nfovorite songs are:{favorite_songs}")

# TUPLE WITHOUT PARENTHESIS
name = 'Dhananjay', 'shivam', 'nikhil'
# print(name)
print(type(name))