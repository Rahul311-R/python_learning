sentence = "the cat sat on the mat the cat sat"

s = sentence.split()


print(set(s))

print(f"Total unique: {len(set(s))}")