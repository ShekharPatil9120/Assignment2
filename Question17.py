# Program: Matrix addition
# Description: Adds two matrices

rows = int(input())                    # number of rows
cols = int(input())                    # number of columns

A = []                                 # first matrix
B = []                                 # second matrix

for i in range(rows):                  # input matrix A
    row = list(map(int, input().split()))
    A.append(row)

for i in range(rows):                  # input matrix B
    row = list(map(int, input().split()))
    B.append(row)

result = []                            # result matrix

for i in range(rows):                  # add matrices
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:                     # print result
    print(*row)