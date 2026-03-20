names  = ["Rahul", "Priya", "Arjun", "Sneha", "Vijay"]
marks  = [78, 92, 56, 88, 45]
ages   = [22, 21, 23, 22, 24]

zipped = zip(names,marks,ages)
print(list(zipped))

zipp = zip(names,marks)
print(dict(zipp))

na = sorted(names)
print(na)
print(names)

d = sorted(marks)
print(d[::-1])

a = sorted(names)
a.sort(key = len)
print(a)

pairs = list(zip(names, marks))
pairs.sort(key=lambda x: x[1])
print(pairs)


pair = zip(names,marks)

na,mo = zip(*pair)
print(na)
print(mo)