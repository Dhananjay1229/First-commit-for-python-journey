# square
# o/p --> {1:1, 2:4, 3:9}

# square = {}
# for i in range(1,4):
#     square[i] = i**2
# print(square)

square_2 = { i : i**2 for i in range(1,5)}  # key : value pair
# print(square_2)     # {1: 1, 2: 4, 3: 9, 4: 16}
# o/p --> square of 1 is 1

# for i,j in square_2.items():
    # print(f"square of {i} is {j}")
    # print(i)


# i --> (1,1)
# i,j --> 1 1   # unpacking 




# "Dhananjay" -- D:1, h:1 etc
name = "Dhananjay"
name_sep = {}
for i in name:
    name_sep[i] = name.count(i)
# print(name_sep)

name_2 = {i:"Dhananjay".count(i) for i in "Dhananjay"}
print(name_2)