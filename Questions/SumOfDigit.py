a = int(input())
s = 0
while a > 0:
    b = a % 10
    s = s + b
    a = a // 10

print(s) 