lines = ["apple\n", "banana\n", "mango\n"]

with open("fruits.txt", "w") as f:
    f.writelines(lines)
