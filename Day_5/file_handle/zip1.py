names = list(map(str,input().split()))
marks = list(map(int,input().split()))

for n, m in zip(names, marks):
    print(n, m)
