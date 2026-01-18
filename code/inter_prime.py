a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))

for i in range(a,b+1):
    if i >1:
        for y in (2,i):
            if i % y == 0:
                break
            else:
                print(i)