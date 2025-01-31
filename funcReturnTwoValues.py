def add_mul(a,b):
    add = a + b
    mul = a * b
    return add,mul

# print(add_mul(2,3)) # it will always return a tuple 
# but for countering this we can use tuple unpacking
add,mul = add_mul(2,3)
print(f"{add} \n{mul}")

