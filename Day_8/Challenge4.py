nums = [3, 7, 1, 9, 4, 9, 6, 2]

lar = nums[0]
sec = nums[0]
for i in nums:
    if lar < i:
        sec = lar
        lar = i
    elif i > sec and lar > i:
        sec = i
print(sec)
