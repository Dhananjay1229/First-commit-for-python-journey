# tuples are all same as lists but IMMUTABLE
# no append, no insert, no del, no remove, no pop

example = (0,1,"Dhananjay",4.5,[3,4])

# print(example)
# print(example[4])
# print(len(example))
# print(example[::-1])
# print(example[0:4:2])
# print(example[0:3])

for i in example:
        if i == "Dhananjay":
            print(example.index(i))

i = 0
while i < len(example):
    if example[i] == "Dhananjay":
        print(i)
    i += 1


