name = ["aab" , "sdf" , "erf" , "inn"]

print(name[0])
print(name[-1])

name.append("efger")

print( name[-1])
print(name)

name.remove("erf")
name.insert(3,"ertgwer")

print(name)

for it in name:
    print(it)
