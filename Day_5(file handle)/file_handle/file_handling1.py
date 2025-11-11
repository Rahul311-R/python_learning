with open("rahul.txt","a") as f:
    f.write("3rd line\n")

with open("rahul.txt","r") as f :
    ct = f.read()
    print(ct)