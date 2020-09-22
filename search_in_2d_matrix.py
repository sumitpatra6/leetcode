def search_2d_grid(grid, startX, startY, endX, endY, target):
    """
    f our target is equal to the pivot, we have found our target and immediately return the result.
    If our target is less than the pivot, we can discard the bottom-right sub-matrix. All elements in that region must be greater or equal than the pivot.
    If our target is greater than the pivot, we can discard the top-left sub-matrix. All elements in that region must be less than or equal than the pivot.
    """
    pivotX = int((startX + endX) / 2)
    pivotY = int((startY + endY) / 2)
    if grid[pivotX][pivotY] == target:
        return True
    if startX == endX and startY == endY:
        pass



grid = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
starting = [0,0]
ending = [len(grid), len(grid[0])]
search_2d_grid(grid, 0, 0, len(grid), len(grid[0]))