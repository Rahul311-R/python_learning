with open("profile.txt", "w") as f:
    f.write("Name: Rahul\n")
    f.write("College: VSB Engineering")
with open("profile.txt", "a") as f:
    f.write("\nAge: 21")
with open("profile.txt", "r") as f:
    print(f.read())
with open("profile.txt", "r") as f:
    for line in f:
        print(line.strip())
