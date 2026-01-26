def occ(li,el):
    ou = li.count(el)
    return ou

num = list(map(int,input().split()))
el = 3
co = occ(num,el)
print(f"the element {el} is occured {co} times")