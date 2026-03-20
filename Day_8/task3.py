students = ["Rahul", "Priya", "Arjun", "Priya", "Sneha", "Priya"]
students.remove("Priya")
while "Priya" in students:
    students.remove("Priya")
if "Vijay" in students:
    students.remove("Vijay")
else:
    print("Vijay is not found")
print(students)