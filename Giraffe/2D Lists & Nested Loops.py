#2D Lists & Nested Lists

# Example 1
number_grid = [
# Coloumns
#    0  1  2
    [1, 2, 3], # Row 0
    [4, 5, 6], # Row 1
    [7, 8, 9], # Row 2
    [0]        # Row 3
]
print (number_grid[2][1])

# Example 2
for row in number_grid:
    print (row)

# Example 3
for row in number_grid:
    for col in row:
        print(col)