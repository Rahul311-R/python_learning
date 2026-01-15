a = input()
v = 0
c = 0

for i in a:
    if i in 'aeiouAEIOU':
        v = v + 1
    else:
        c = c + 1

print("vowel=", v)
print("con=",c)
