words = ["apple", "banana", "apple", "cherry", "banana", "mango", "cherry"]

a = []
for i in words:
    if i not in a:
        a.append(i)

print(a)