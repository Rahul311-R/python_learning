a = list(map(int,input().split()))
k = int(input())
if k == 0 or k>= len(a):
    print("Invalid value to rotate")
else:
    lar = a[:k]
    se = a[k:]
    ro = se + lar
    print(*ro)