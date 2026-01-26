num = list(map(int,input().split()))
sm = num[0]
for i in num:
    if sm > i:
        sm = i

print(sm)