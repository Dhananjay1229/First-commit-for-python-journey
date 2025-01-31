name,age = input("Type your Name and Age ").split() # .split() func for taking two inputs on same line 
print("Hello"+ " " +name+ " "+ "Your Age is: "+age) # lengthy
print("Hello {} Your Age is: {}".format(name,age)) # using place holder and .format() function # no need to adjust data type string-->number
print(f"Hello {name} Your Age is: {age}") # f for .format() function

