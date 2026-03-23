students = [
    ("Rahul", 22, 78),
    ("Priya", 21, 92),
    ("Arjun", 23, 56),
    ("Sneha", 22, 88)
]

for name,age,mark in students:
    print(f"{name} is {age} years old and scored {mark}")

lar = students[0][2]
nam = students[0][0]

for name,age ,mark in students:
    if lar < mark:
        lar = mark
        nam = name

print(f"Topper is {nam} with {lar} marks")

names = [name for name,age,marks in students]

marks = [mark for name,age,mark in students]

print(names)

print(marks)

first , *rest  = students

print(first)
print(rest)
name,age,ma = first
print(f"{name}, {age} ,{ma}")