# fibonacci series
# 0 1 1 2 3 5 8 13 21 34

def fibonacci_seq(n):
    a = 0   # first number  # a = 1 # a = 1 # a = 2
    b = 1   # second number # b = 1 # b = 2 # b = 3
    if n == 1:
        print(a)    
    elif n == 2:
        print(a, b)
        
    else:
        print(a, b, end=" ") # n = 3--> 0 1 ?1 # n = 4--> 0 1 ?1 ?2 # n = 5--> 0 1 ?1 ?2 ?3
        for i in range(n-2):
            c = a + b   # 1 # 2
            a = b       # 1 # 1
            b = c       # 1 # 2
            print(b, end=" ") # 1 # 2

        
fibonacci_seq(64)
       


















# fibonacci series
# 0 1 1 2 3 5 8 13 21 34




# print(x,y)

def fib(n):
    x = 0
    y = 1
    if n == 1:
        print(x)
    elif n==2:
        print(x,y,end =" ")
    else:
        print(x,y, end = " ")
        for i in range(n-2):
            c = x + y
            x = y
            y = c
            print(y, end = " ")


# fib(10)