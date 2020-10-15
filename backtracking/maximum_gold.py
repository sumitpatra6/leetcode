def getMaximumGold(grid):
    def util(x, y, visited):
        if x >= len(grid) or y >= len(grid[0]) or x< 0 or y < 0 or grid[x][y] == 0 or [x,y] in visited:
            return 0, visited
        visited.append([x, y])
        current_value = grid[x][y]
        # try to go left
        left_value, left_visited = util(x, y-1, visited)
        # try to go right
        right_value, right_visited = util(x, y+1, visited)
        # try to go up 
        up_value, up_visited = util(x-1, y, visited)
        # try to go down
        down_value, down_visited = util(x+1, y, visited)
        max_collected = 0
        max_visited = []
        if left_value + current_value> max_collected:
            max_collected = left_value + current_value
            max_visited = left_visited
        if right_value + current_value > max_collected:
            max_collected = right_value + current_value
            max_visited = right_visited
        if up_value + current_value > max_collected:
            max_collected = up_value + current_value
            max_visited = up_visited
        if down_value + current_value > max_collected:
            max_collected = down_value + current_value
            max_visited = down_visited
        return max_collected, max_visited
    
    rows = len(grid)
    cols = len(grid[0])
    max_collected = 0
    max_visited = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i == 2 and j == 0:
                    print("Debug point")
                collected, visited = util(i, j, [])
                if collected > max_collected:
                    max_collected = collected
                    max_visited = visited
                
    print(max_collected, max_visited)
    return max_collected


grid = [[0,6,0],[5,8,7],[0,9,0]]
# grid =  [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# grid = [
# [0,0,0,0,0,0,32,0,0,20],
# [0, 0,   2,0,0,0,0,40,0,32],
# [13,20,36,0,0,0,20,0,0,0],
# [0, 31,27,0,19,0,0,25,18,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,18,0,6],
# [0,0,0,25,0,0,0,0,0,0],
# [0,0,0,21,0,30,0,0,0,0],
# [19,10,0,0,34,0,2,0,0,27],
# [0,0,0,0,0,34,0,0,0,0]]

getMaximumGold(grid)
