a = list(map(int,input().split()))
lar = a[0]
for i in a:
    if lar < i:
        lar = i
print(lar)