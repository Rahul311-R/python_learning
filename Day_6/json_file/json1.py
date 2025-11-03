import json
data = {
    "name" : "Rahul",
    "age":21,
    "dept":"AI"
}
js = json.dumps(data)
print(js)