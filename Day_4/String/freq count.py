txt = input().split()
count = {}
for wo in txt:
    if wo in count:
        count[wo] += 1
    else:
        count[wo] = 1

print(count)

#from collections import Counter
#print(Counter(input().split()))
