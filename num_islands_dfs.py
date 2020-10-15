grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid3 = [["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]]

class Solution:
    def dfs(self, grid, i, j):
        if self.visited[i][j] == 1:
            return
        self.visited[i][j] = 1
        if i - 1 >= 0 and self.visited[i-1][j] != 1 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if i + 1 < self.num_rows and self.visited[i+1][j] != 1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j - 1 >= 0 and self.visited[i][j-1] != 1 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)
        if j+1 < self.num_columns and self.visited[i][j+1] != 1 and grid[i][j+1] =='1':
            self.dfs(grid, i, j+1)



    def numIsLands(self, grid):
        islands = 0
        self.num_rows = len(grid)
        self.num_columns = len(grid[0])
        self.visited = []
        for i in range(self.num_rows):
            self.visited.append([0]*self.num_columns)
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.visited[i][j] != 1 and grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1
        print(self.visited)
        return islands
sol = Solution()
print(sol.numIsLands(grid3))