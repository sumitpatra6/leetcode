from collections import deque


def flood_fill(image, sr, sc, newColor):
    row_count = len(image)
    col_count = len(image[0])
    visited = []
    original_color = image[sr][sc]
    visited.append([sr, sc])
    q = deque()
    q.append([sr, sc])
    while len(q) > 0:
        i, j = q.popleft()
        image[i][j] = newColor
        visited.append([i,j])
        if i - 1 >= 0 and image[i-1][j] == original_color and [i-1, j] not in visited:
            q.append([i-1, j])
        if i + 1 < row_count and image[i+1][j] == original_color and [i+1, j] not in visited:
            q.append([i+1, j])
        if j - 1 >= 0 and image[i][j-1] == original_color and [i, j - 1] not in visited:
            q.append([i, j-1])
        if j+1 < col_count and image[i][j+1] == original_color and [i, j+1] not in visited:
            q.append([i, j+1])
    print(image)

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# newColor = 2
image = [[0,0,1],[0,1,1]]
sr = 1
sc = 1
newColor = 1
flood_fill(image, sr, sc, newColor)