def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i

    return fac

a = int(input("Enter the number:"))
print(fact(a))