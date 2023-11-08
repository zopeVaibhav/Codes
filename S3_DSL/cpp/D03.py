X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows 
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("The Addition of two matrix is: ")
for r in result:
    print(r)
# Subtraction of matrices
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
print("The Substraction of two matrix is: ")
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]
for r in result:
    print(r)
# Multiplication of matrices
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
print("The Multiplication of two matrix is: ")
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
     # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)
# Transpose of matrix
X = [[12, 7],
     [4, 5],
     [3, 8]]
result = [[0, 0, 0],
          [0, 0, 0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
print("The Transpose of two matrix is: ")
for r in result:
    print(r)
