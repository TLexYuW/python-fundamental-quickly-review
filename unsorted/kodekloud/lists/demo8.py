Colors = [
    [["Blue", "Green", "White", "Black"]],
    [["Green", "Blue", "White", "Yellow"]],
    [["White", "Blue", "Red", "Green"]],
]

print(Colors[2][0][2])


# matrix3 = [[[k for k in range(3)] for j in range(3)] for i in range(3)]

matrix3 = []

for i in range(3):
    inner_matrix = []
    for j in range(3):
        row = []
        for k in range(3):
            row.append(k)
        inner_matrix.append(row)
    matrix3.append(inner_matrix)

print(matrix3)
print(matrix3[0][0][1])


matrix4 = [
    [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
    [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
    [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
]

matrix5 = []

for submatrix in matrix4:
    for val in submatrix:
        matrix5.append(val)

print(matrix5)
print(matrix5[2][0])
