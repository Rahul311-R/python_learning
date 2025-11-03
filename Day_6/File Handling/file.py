with open("data.txt","w") as r:
    r.write("1st line\n")
    r.write("2nd line\n")
    r.write("3rd line\n")

with open("data.txt","a") as f:
    f.write("4th line\n")

with open("data.txt","r") as t:
    li = t.read()
    print(li)