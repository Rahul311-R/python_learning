nums = list(map(int,input().split()))

lar = nums[0]
sec = nums[0]
for i in nums:
    if lar < i:
        sec = lar
        lar = i
    elif i > sec and lar > i:
        sec = i
print(sec)