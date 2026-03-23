pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

n = list()
a = list()
 
for num ,al in pairs:
    n.append(num)
    a.append(al)

print(set(n))
print(set(a))