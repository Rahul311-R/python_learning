def calc(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a/b

print(calc(345,4543,"+"))