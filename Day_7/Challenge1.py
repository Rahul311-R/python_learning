import random

n = random.randint(1,100)
while True:
    a = int(input("Guess:"))
    if a<n:
        print("Too low")
    elif a>n:
        print("Too high")
    else:
        print("You got it")
        break