li = [[1,2],[3,4],[5,6]]
l = []
for a in li:
    for o in a:
        l.append(o)

print(l)

l = [o for a in li for o in a]
print(l)
