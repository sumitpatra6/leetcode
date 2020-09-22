def nullify_row(grid, row, col_count):
    for i in range(col_count):
        grid[row][i] = 0
    return grid

def nullify_column(grid, col, row_count):
    for i in range(row_count):
        grid[i][col] = 0
    return grid

def fill_zero(grid):
    row_count = len(grid)
    col_count = len(grid[0])
    # check if the first row and first column has zeros
    row_has_zeros = False
    col_has_zeros = False
    for i in range(col_count):
        if grid[0][i] == 0:
            row_has_zeros = True
            break
    for i in range(row_count):
        if grid[i][0] == 0:
            col_has_zeros = True
            break
    print(col_has_zeros, row_has_zeros)
    # now traverse through all the remaining elements
    for i in range(1,row_count):
        for j in range(1, col_count):
            if grid[i][j] == 0:
                grid[0][j] = 0
                grid[i][0] = 0
    print(grid)
    # now do the second pass
    for i in range(row_count):
        if grid[i][0] == 0:
            grid = nullify_row(grid, i, col_count)
    for i in range(col_count):
        if grid[0][i] == 0:
            grid = nullify_column(grid, i, row_count)
    print(grid)
    if col_has_zeros:
        grid = nullify_column(grid, 0, row_count)
    if row_has_zeros:
        grid = nullify_row(grid, 0, col_count)
    print(grid)


grid = [[1,2,3], [4,0,6], [7,8,9]]
fill_zero(grid)
