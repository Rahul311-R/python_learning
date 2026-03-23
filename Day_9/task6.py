str1 = "listen"
str2 = "silent"
str3 = "hello"
a = sorted(str1)
b = sorted(str2)
c = sorted(str3)

if (a == b) and (a != c):
    print('''listen and silent are anagrams!
          listen and hello are NOT anagrams!''')