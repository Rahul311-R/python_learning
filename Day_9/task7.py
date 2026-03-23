nums = [1, 5, 3, 4, 2, 8, 6]
k = 2

num_set = set(nums)  

pairs = []
for num in nums:
    if num+k in num_set:    
        pairs.append((num,num+k)) 

pairs.sort()   
for pair in pairs:
    print(pair)