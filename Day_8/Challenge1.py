number = [5,6,4,3,2,5467,8,5,3]

lar = list[0]
sml = list[0]
for i in list:
    if lar < i:
        lar = i
    if sml > i:
        sml = i
    else:
        continue
print("Max:",lar)
print("Min:",sml)