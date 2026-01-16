def average(*n):
    to = 0
    for i in n:
        to += i

    return to / len(n)



print(average(10, 20, 30))