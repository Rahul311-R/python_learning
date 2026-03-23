nums = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1, 8, 9, 1]

a = []

for i in nums:
    if nums.count(i)>1:
        a.append(i)

print(f"Duplicates: {set(a)}")

for i in set(a):
    print(f"{i} appears {nums.count(i)} times")