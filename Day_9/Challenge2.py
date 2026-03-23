python_students = {"Rahul", "Priya", "Arjun", "Sneha", "Vijay"}
java_students   = {"Arjun", "Sneha", "Vijay", "Meera", "Kumar"}
print(python_students&java_students)

print(python_students-java_students)

print(java_students-python_students)

print(python_students|java_students)

print(python_students^java_students)

print({"Arjun", "Sneha"}.issubset(python_students))

python_students.add("Deepa")

java_students.discard("Vijay")

print(python_students)

print(java_students)