from collections import deque
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


def num_islands(grid):
    visited = []
    q = deque()
    islands = 0
    num_rows = len(grid)
    num_columns = len(grid[0])
    for i in range(0, num_rows):
        for j in range(0, num_columns):
            if [i,j] not in visited and grid[i][j] == '1':
                islands += 1
                q.append([i,j])
                visited.append([i,j])
            while len(q) > 0:
                current_node = q.popleft()
                current_i = current_node[0]
                current_j = current_node[1]
                print("visiting node {}".format(current_node))
                # check for all 4 directions
                if current_i - 1 >= 0 and grid[current_i-1][current_j] == '1' and [current_i - 1, current_j] not in visited:
                    visited.append([current_i - 1, current_j])
                    q.append([current_i - 1, current_j])
                if current_i+1 < num_rows and grid[current_i+1][current_j] == '1' and [current_i+1, current_j] not in visited:
                    # row below
                    visited.append([current_i+1, current_j])
                    q.append([current_i + 1, current_j])
                if current_j - 1 >= 0 and grid[current_i][current_j - 1]== '1' and [current_i, current_j - 1] not in visited:
                    # columns before
                    visited.append([current_i, current_j - 1])
                    q.append([current_i, current_j - 1])
                if current_j + 1 < num_columns and grid[current_i][current_j + 1]== '1' and [current_i, current_j + 1] not in visited:
                    # column after 
                    visited.append([current_i, current_j +1])
                    q.append([current_i, current_j +1])
    print(islands)
    
num_islands(grid)

