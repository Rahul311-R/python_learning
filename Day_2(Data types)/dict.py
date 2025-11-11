data = {"name":"rahul","age":21,"dept":"Ai&Ds"}
print(data["name"])
data["college"] = "VSB"
print(data)

data["dept"] = "AI"
print(data)

for key, value in data.items():
    print(key, ":", value)
