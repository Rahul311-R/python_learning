with open("notes.txt","a") as f:
    f.write("\nthis is the third line")

with open("notes.txt","r") as r:
    a = r.read()
    print(a)