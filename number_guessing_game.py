import random
# BY INTRODUCING BREAK
# winning_number = random.randint(0,100)
# user_number = int(input("Guess a number b/w 0 to 100: "))  
# guess = 0
# while True:
#     if user_number == winning_number:   
#         print(f"YOU WIN !!!!,and you guessed thin number in {guess} times")
#         break
#     elif user_number < winning_number:
#         print("too low")
#         user_number = int(input("Guess again: "))
#         guess += 1
#     else:
#         print("too high")  
#         user_number = int(input("Guess again: "))
#         guess += 1

# BY MAKING THE LOOP FALSE WHEN YOU MAKE THE RIGHT GUESS
winning_num = random.randint(0,100)
guess = 0
num = int(input("Guess a number between 0 to 100: "))
game_over = False 
while not game_over: # it means while not False i.e while is True ---> infinite loop until while False 
    if num == winning_num:
        print(f"You Win!\nYou guessed the number in {guess} attempt/s")
        game_over = True # it means the loop stops when while nit True executes by changing game_over value
    elif num < winning_num:
        print("Too Low!")
        num = int(input("Guess again: ")) 
        guess += 1
    else:
        print("Too High!")
        num = int(input("Guess again: ")) 
        guess += 1
        
# By introducing continue 
# winning_num = random.randint(0,100)
# guess = 0
# game_over = False 
# while not game_over: # it means while not False i.e while is True ---> infinite loop until while False 
#     num = int(input("Guess a number between 0 to 100: "))
#     if num == winning_num:
#         print(f"You Win!\nYou guessed the number in {guess} attempt/s")
#         game_over = True # it means the loop stops when while nit True executes by changing game_over value
#     elif num < winning_num:
#         print("Too Low!")
#         guess += 1
#         continue
#     else:
#         print("Too High!")
#         guess += 1
#         continue
        
        



    
        




