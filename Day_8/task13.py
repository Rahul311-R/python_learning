import copy
o = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = o
print(id(a))
print(id(o))

b = o.copy()
b.append([34,445,5])
print(o)
print(b)

c = copy.deepcopy(o)
print(o)
print(c)

print(id(o))
print(id(a))
print(id(b))
print(id(c))