class Solution:
    # m is row and n is column
    def min_path(self, grid, i, j,m,n, value):
        if i== m -1 and j == n-1:
          value += grid[i][j]
          return value
        if i >= m or j >= n:
          return float('inf')
        value += grid[i][j]
        return min(self.min_path(grid, i+1, j, m, n, value), self.min_path(grid, i, j+1, m, n, value)) 

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        answer = [[0]*n for x in range(m)]
        answer[0][0] = grid[0][0]
        for i in range(m):
          for j in range(n):
            # print(answer)
            if i ==0 and j == 0:
              #already processed
              continue
            if j - 1 < 0:
              answer[i][j] = answer[i-1][j] + grid[i][j]
            elif i -1 < 0:
              answer[i][j] = answer[i][j-1] + grid[i][j]
            else:
              answer[i][j] = grid[i][j] + min(answer[i-1][j], answer[i][j-1])

        # print(answer)
        print('-------')
        return answer[m-1][n-1]
        


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
sol = Solution()
print(7)
print(sol.minPathSum(grid))
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
import time
t = time.time()
print(sol.minPathSum(grid))
print(time.time() - t)