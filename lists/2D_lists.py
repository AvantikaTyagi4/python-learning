matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# to print any row from list
print(matrix [0])

# print any element from list like at  1 st row and 2nd column
print(matrix[0][1])

# to modify any item in matrix
matrix[0][1] = 50

# to iteate over matrix
for row in matrix:
    for item in row:
        print(item)