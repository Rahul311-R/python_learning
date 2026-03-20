matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

rows = len(matrix)
cols = len(matrix[0])
mid  = rows // 2

# Task 1 — dimensions
print(f"Dimensions: {rows} x {cols}")

# Task 2 — four corners
print(f"Corners: {matrix[0][0]}, {matrix[0][-1]}, {matrix[-1][0]}, {matrix[-1][-1]}")

# Task 3 — center
print(f"Center: {matrix[mid][mid]}")

# Task 4 — middle row
print(f"Middle row: {matrix[mid]}")

# Task 5 — middle column
mid_col = [matrix[i][mid] for i in range(rows)]
print(f"Middle column: {mid_col}")

# Task 6 — sum of all
total = sum(matrix[i][j] for i in range(rows) for j in range(cols))
print(f"Total sum: {total}")

# Task 7 — sum of each row
for i, row in enumerate(matrix):
    print(f"Row {i} sum: {sum(row)}")

# Task 8 — sum of each column
for j in range(cols):
    col_sum = sum(matrix[i][j] for i in range(rows))
    print(f"Col {j} sum: {col_sum}")

# Task 9 — main diagonal
diagonal = [matrix[i][i] for i in range(rows)]
print(f"Main diagonal: {diagonal}")

# Task 10 — anti diagonal
anti = [matrix[i][cols-1-i] for i in range(rows)]
print(f"Anti diagonal: {anti}")

# Task 11 — transpose
transposed = [list(row) for row in zip(*matrix)]
print(f"Transposed: {transposed}")

# Task 12 — elements greater than 15
big = [matrix[i][j] for i in range(rows) for j in range(cols) if matrix[i][j] > 15]
print(f"Greater than 15: {big}")
