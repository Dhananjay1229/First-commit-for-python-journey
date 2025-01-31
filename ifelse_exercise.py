# Exercise , Number Guessing Game 



# Make a variable, like winning number and assign any number to it 
winning_number = 7

# Ask user to guess a number
user_number = int(input("Type a number b/w 0 to 9: "))  

# if user guessed correctly then print "YOU WIN !!!!"
if user_number == winning_number:   # == for checking equality
    print("YOU WIN !!!!")

# if user didn't guessed correctly then:
#     if user guessed lower than actual then print "too low"
#     if user guessed higher than actual number then print "too high"
else:                   # NESTED IFELSE STATEMENT
    if user_number < winning_number:
        print("too low")
    else:
         print("too high")

# google "how to generate random number in python" to generate random winning_number




    