def user_info(first_name,last_name = 'unknown',age = 'unknown'): # we can make any parameter default to not counter positional argument error 
    # non-default argument follows default argument error (first_name,last_name = 'unknown',age)
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info("Dhananjay")


    