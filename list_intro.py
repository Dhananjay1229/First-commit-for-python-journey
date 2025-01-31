# used for storing string, int, float anything

num = [1, 2, 3]
print(num)

string = ["four", "five", "six"]
print(string)

mixed = [7, 'eight', 9.0]
print(mixed)

print(num[1])       # indexing
print(string[:2])   # slicing
print(mixed[-1])    # negative indexing

mixed[2] = "nine"
print(mixed)

string[0:] = 4, 5, 6
print(string)

string[0:] = "seven","eight","nine"
print(string)
