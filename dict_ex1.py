# define a function that takes a number 
# return a dictionary containing cube of numbers from 1 to n 

# example 
# cube_finder(3)
# {1:1, 2:8, 3:27}

n = int(input("Enter any number: "))
cubes = list(range(1,n+1))
# def cube_finder (a):
#     cube_finder =[]
#     for i in a:
#         cube_finder.append(i**3)
#     return cube_finder

# print(cube_finder(cubes))

# def cube_finder(a):
#     cube_finder = {}
#     for i in a:
#         cube_finder[i] = i**3
#     return cube_finder
# print(cube_finder(cubes))

# alternate solution 
def cube_finder (n):
    cube_finder = {}
    for i in range(1,n+1):
        cube_finder[i] = i**3
    return cube_finder
print(cube_finder(5))