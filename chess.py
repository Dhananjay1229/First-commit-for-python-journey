# 1 2 4 8 16 32

def chess(n):
    a = 1  # 2 # 4
    if n == 1:
        print(a)
    else:
        print(a, end=" ") # 1 ?2 ?4 ?8
        for i in range(n-1):
            c = a + a # 2 # 4 # 8
            a = c     # 2 # 4 # 8
            print(a, end=" ") # 2 # 4 # 8
    
    

        
# chess(64)
       






























#  1 2 4 8 16 32

def Sambhajis_game():
    grains_num = []
    x = 1
    grains_num.append(x)
    for i in range (64):
        y = x + x
        x = y
        grains_num.append(y)
    return grains_num




grains = Sambhajis_game()


# print(grains)

# print(grains[-1]) # 18446744073709551616

kgs = grains[-1]/50000

# print(kgs)

tonne = kgs/1000

# print(tonne)


megatonne = tonne/10000000

# print(megatonne)

# print(round(megatonne))





# class chess:
#     def Sambhajis_game():
#         grains_num = []
#         x = 1
#         grains_num.append(x)
#         for i in range (64):
#             y = x + x
#             x = y
#             grains_num.append(y)
#         return grains_num


# grains = chess()
# no_of_grains = grains.Sambhajis_game()
# print(no_of_grains)





