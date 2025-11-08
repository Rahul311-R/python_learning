with open("pointer_demo.txt", "w") as f:
    f.write("Artificial Intelligence and Data Science")

with open("pointer_demo.txt", "r") as f:
    print("Position:", f.tell())      # start at 0
    print(f.read(10))                 # read first 10 characters
    print("After reading:", f.tell()) # new position
    f.seek(0)                         # move back to start
    print("After seek:", f.tell())
    print(f.read())                   # read entire content again
