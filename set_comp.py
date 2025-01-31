s = set(range(1,11))
# print(s)

s2 = {i for i in range(1,11)}
# print(s2)

s3 = set(i**2 for i in range(1,11))
# print(s3)                           # unordered 
# print(type(s3))

names = {'Dhananjay', 'shivam','Nikhil'}
# for name in names:
#     print(name[0])
initials = {name[0] for name in names}
print(initials)

