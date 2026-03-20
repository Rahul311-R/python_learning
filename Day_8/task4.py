scores = [45, 78, 92, 56, 78, 88, 92, 71]
scores.index(92)
scores.index(78,2)
for i in scores:
    if i == 92:
        print(scores.index(92))
if 100 in scores:
    print(scores.index(100))
else:
    print("100 not found")