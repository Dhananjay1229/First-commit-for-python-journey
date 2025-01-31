# checks two conditions at the same time 

name = "Dhananjay"
age = 30           # when we assign int to variable it will take it as int but when we use input function to assign an int it always take it as string

if name == "Dhananjay" and age == 30: 
# with and operator both conditions have to be true 
    print("Condition is True")
else:
    print("Condition is False")

if name == "Dhananjay" or age == 18:
# with or operator either of the one condition has to be true 
    print("Condition is True")
else:
    print("Condition is False")