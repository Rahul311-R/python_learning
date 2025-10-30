def maximum(a, b, c):
    if a >= b+ c:
        return a
    elif b >= a + c:
        return b
    else:
        return c

print(maximum(1, 2, 3))