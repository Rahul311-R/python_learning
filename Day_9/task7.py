nums = [1, 5, 3, 4, 2, 8, 6]
k = 2

num_set = set(nums)   # convert to set for fast lookup

pairs = []
for num in nums:
    if num+k in num_set:        # check if num+k exists
        pairs.append((num,num+k))  # add pair in ascending order

pairs.sort()   # sort pairs
for pair in pairs:
    print(pair)