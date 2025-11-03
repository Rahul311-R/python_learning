import json

data = {
    "Name":"Rahul",
    "Age":21,
    "college":"VSB"
}

with open("Profile.json","w") as f:
    json.dump(data,f)

with open("Profile.json","r") as t:
    vi = t.read()
    print(vi)