steps = ["wake up", "brush teeth", "shower", "breakfast", "go to work"]

# Task 1 — original
print("Original:", steps)

# Task 2 — reverse()
steps.reverse()
print("Reversed:", steps)

# Task 3 — reset and prove [::-1] safe
steps = ["wake up", "brush teeth", "shower", "breakfast", "go to work"]
new = steps[::-1]
print("New list:", new)
print("Original unchanged:", steps)

# Task 4 — sort then reverse
steps = ["wake up", "brush teeth", "shower", "breakfast", "go to work"]
steps.sort()
print("After sort:", steps)
steps.reverse()
print("After sort+reverse:", steps)