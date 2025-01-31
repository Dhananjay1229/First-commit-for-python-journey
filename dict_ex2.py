# take data from user 
# user_info = {
#     'name':'Dhananjay',
#     'age': 30,
#     'fav_movies':['godfather','interstellar'],
#     'fav_songs':['sunflower','heathens']
# }

# save it in a dictionary 
# string , integer , a list 
# comma separated values 

user = {}
user['name'] = input("Type your name:")
user['age'] = int(input("Enter your age:"))
user['fav_movies'] = list(input("Enter your fav movies separated by comma: ").split(","))
user['fav_songs'] = list(input("Enter your fav songs separated by comma: ").split(","))

# for i in user.items():
#     print(i)
# OR
for i,j in user.items():
    print(f"Your {i} is/are {j}")




# for i in user:
#     print(i)        # will only print keys 

# print(user)
# {'name': 'Dhananjay', 'age': 30, 'fav_movies': ['godfather', ' interstellar'], 'fav_songs': ['sunflower,heathens']}
# not like this 
# like name : Dhananjay