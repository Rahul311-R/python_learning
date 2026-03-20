s = [
    ["Rahul", 22, 78],
    ["Priya", 21, 92],
    ["Arjun", 23, 56],
    ["Sneha", 22, 88],
    ["Vijay", 24, 45]
]

print(s[1][2])
print(s[2][1])
for i in range(len(s)):
    print(s[i][0])

for i in range(len(s)):
    print(s[i][2])

a = []
for i in range(len(s)):
    a.append(s[i][2])
print(max(a))


for i in range(len(s)):
    if (s[i][1]) == 22:
        print(s[i][0])

s[-1][2] = 75

s.append(["Meera", 20, 95])

print("Name  Age  Mark")

for i in range(len(s)):
    print(f"{s[i][0]}  {s[i][1]}  {s[i][2]}")