import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row_input = input(f"Enter {cols} elements for row {i+1}, separated by spaces: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)

a = np.array(matrix)

print("\nYour 2D array:")
print(a)

print("\nReversed array:")
print(a[::-1, ::-1])

print("\nPrincipal diagonal elements:")
print(np.diag(a))

print("\nSorted in ascending order:")
print(np.sort(a))

print("\nSorted in descending order:")
print(np.sort(a)[:, ::-1])
