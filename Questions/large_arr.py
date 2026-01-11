a = list(map(int,input().split()))
lar = a[0]
for i in range(1,len(a)):
    if lar<a[i]:
        lar = a[i]
    
print(lar)