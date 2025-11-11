try:
    # risky code
    f = open("no_file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("That file doesn't exist, creating it now...")
    with open("no_file.txt", "w") as f:
        f.write("New file created automatically.")
