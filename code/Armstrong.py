n = int(input())
t = n
sum = 0
digit = len(str(n))
while t > 0:
    a = t % 10
    sum += a ** digit
    t //=  10

if sum == n:
    print("It is a armstrong")
else:
    print("It is not a armstrong")