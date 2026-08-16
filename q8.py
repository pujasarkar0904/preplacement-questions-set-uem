rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("Transpose of matrix:")

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()