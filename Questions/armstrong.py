a = int(input())
temp = a
sum = 0
d = 0
while a > 0:
    d = d + 1
    a = a // 10
a = temp
while a > 0 :
    b = a % 10
    sum = sum + b ** d
    a = a // 10 
if sum == temp:
    print("it is a armstrong number")
else:
    print("it is not a armstroong number")