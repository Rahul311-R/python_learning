def even(r):
    for i in range(r+1):
        if i%2==0:
            print(i)


a = int(input("Enter a number:"))
print(even(a))