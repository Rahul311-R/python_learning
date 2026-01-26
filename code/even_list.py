num = list(map(int,input().split()))
li = []
for i in num:
    if i % 2 == 0:
        li.append(i)
print(*li)