with open("rahul.txt","a") as r:
    r.write("the only king\n")

with open("rahul.txt","r") as t:
    rt = t.read()
    print(rt)