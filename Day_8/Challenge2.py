number = [ 3,55,6,544,43,32,2,32,54,67,45,433,43,32,3]

res = []

for i in number:
    if i not in res:
        res.append(i)

print(res)