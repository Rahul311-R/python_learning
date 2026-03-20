nums = [2, 7, 4, 1, 3, 6]
target = 8
pairs = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):   
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print(pairs)   # [(2, 6), (7, 1)]