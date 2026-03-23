nums = [1, 3, 2, 1, 4, 1, 3, 2, 1, 4, 1]

# Step 1 — unique numbers
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)

# Step 2 — find most frequent
most_frequent = unique[0]
highest_count = nums.count(unique[0])  # start with first item's count!

for n in unique:
    if nums.count(n) > highest_count:  # compare COUNTS not values!
        highest_count = nums.count(n)
        most_frequent = n

print(f"Most frequent: {most_frequent} (appears {highest_count} times)")