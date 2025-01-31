# filter function , iterable
# filter object is iterable -- we can run a loop once 
# filter can verify true false in a loop and filters true's 


# function for extracting even numbers from a list

numbers = [1,2,3,4,5,6,7,8,9]

# method 1 
evens =[]
for i in numbers:
    if i%2 == 0:
        evens.append(i)
print(evens)

# Method 2 
evens2 = [ i for i in numbers if i%2 == 0]
print(evens2)

# Method 2.1 
# new_evens = lambda i : i if i%2 == 0 else break   ---> can't gives o/p
# print(new_evens(numbers))

# Method 3
print(list(filter(lambda i:i%2==0,numbers)))
