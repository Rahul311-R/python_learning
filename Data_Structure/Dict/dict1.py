# Creating a dictionary
student = {"name": "Rahul", "age": 21, "course": "Python"}

print(student["name"])       # Rahul
print(student.get("age"))    # 21
print(student.get("grade"))  # None → safer than indexing

student["grade"] = "A"
student.update({"age":22})
student.pop("course")

for key in student:
    print(key,student[key])