names = ["Rahul", "Priya", "Arjun", "Sneha", "Vijay"]
marks = [78, 92, 56, 88, 45]
for n,m in zip(names,marks):
    print(f"{n}:{m}")
for i,n in enumerate(names):
    print(f"{i}.{n}")
new = []
for n,m in zip(names,marks):
    if m >75:
        new.append(n)
print(new)
lar=marks[0]
for n,m in zip(names,marks):
    if m>lar:
        lar = m
for n,m in zip(names,marks):
    if lar == m:
        print(f"Highest mark: {n}")
ma = marks
for i in range(len(ma)):
    ma[i] = ma[i]*2
print(ma)
for i in reversed(names):
    print(i,end=" ")
print()
for n,m in zip(names,marks):
    if n == "Sneha":
        print(m)