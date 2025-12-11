with open("notes.txt","w") as f:
    f.write("this is the first line.\n")
    f.write("this is the second line.")

with open("notes.txt","r") as r:
    d = r.read()
    print(d)