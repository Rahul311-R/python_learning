def trans(m1):
    row,col = len(m1),len(m1[0])
    res = [[0 for _ in range(row)]for _ in range(col)]

    for i in range(row):
        for j in range(col):
            res[j][i]= m1[i][j]

    return res

matrix = [
 [1, 2, 3],
 [4, 5, 6]
]
print(trans(matrix))