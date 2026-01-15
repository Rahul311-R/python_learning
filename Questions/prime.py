a = int(input())
if a <= 1:
    print("it is not a prime number")
else:
    isprime = True
    for i in range(2,a):
        if a % i == 0:
            isprime = False
            break
    if isprime:
        print("it is a prime number")
    else:
        print("it is not a prime number")