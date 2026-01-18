def max_three(a,b,c):
    if a>(b+c):
        return a
    elif b>(a+c):
        return b
    else :
        return c

print(max_three(56,679,78))