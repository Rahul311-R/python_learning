st = input()
v = 0
c = 0
vo = "aeiouAEIOU"
for ch in st:
    if ch.isalpha():
        if ch in vo:
            v += 1
        else:
            c += 1
print("vowel=",v)
print("consonant=",c)