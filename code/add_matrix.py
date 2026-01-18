def add_mat(m1,m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Matrices must have the same dimensions for addition"
    else:
        a = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                t = m1[i][j] + m2[i][j]
                row.append(t)

            a.append(row)
        return a

m1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

m2 = [
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]

print(add_mat(m1,m2))