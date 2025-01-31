# input 3 numbers from user # try taking 3 inputs in one line separated by comma
# Avg of these 3 numbers
# print avg using string formatting



number1, number2, number3 = input("Type 1st Number and 2nd Number and 3rd Number").split()
# print((int(number1)+int(number2)+int(number3))//3) # lengthily
# print((int(f"{number1}")+int(f"{number2}")+int(f"{number3}"))//3) # lengthily
# print(f"{(int(number1)+int(number2)+int(number3))/3}")
# print("({}+{}+{})//3".format(number1,number2,number3)) # wrong output
# (int(number1)+int(number2)+int(number3))//3  # do the calculations first then put it inside place holder {}
print(f"Average is {(int(number1)+int(number2)+int(number3))//3}") 
print("Average is {}".format((int(number1)+int(number2)+int(number3))//3))


