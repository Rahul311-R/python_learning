def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "0 can not be divided"
    return a/b

print("Enter the operation:")
print("1.addition")
print("2.subtraction")
print("3.multiple")
print("4.divided")

n = int(input("Enter the operation number:"))

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if n == 1:
    print(f"{a} + {b} = {add(a,b)}")
elif n == 2:
    print(f"{a} - {b} = {sub(a,b)}")
elif n == 3:
    print(f"{a} x {b} = {mul(a,b)}")
else:
    print(f"{a} / {b} = {div(a, b)}")