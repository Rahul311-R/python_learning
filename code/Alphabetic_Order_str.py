str = input()
words = [w.capitalize() for w in str.split()]
words.sort()
print(*words)
