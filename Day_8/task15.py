nums   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names  = ["Rahul", "Priya", "Arjun", "Sneha", "Vijay"]
marks  = [78, 92, 56, 88, 45]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

squ = [x ** 2 for x in nums]
print(squ)

a = [x for x in nums if x%3==0]
print(a)

b = ["high" if x > 5 else "low" for x in nums]
print(b)

c = [x.upper() for x in names]
print(c)

d = [x for x in names if len(x)>4 ]
print(d)

e = [(x,len(x)) for x in names]
print(e)

passed = [names[i] for i in range(len(marks)) if marks[i] >= 50]
print(passed)

g = ["Pass" if x >= 50 else "Fail" for x in marks]
print(g)

h = [w for y in matrix for w in y ]
print(h)

m = [(x,y) for x in names for y in marks]
print(m)