def fi(li,k):
    re = []
    for i in li:
        if len(i) > k:
            re.append(i)
    return re

word = list(map(str,input().split()))
k = int(input())
a = fi(word,k)
print(*a)