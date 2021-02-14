"""
1254. Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands/
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
            if grid[i][j] == 0:
                grid[i][j] = 1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0]) - 1)
            
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid[0]) - 1, j)
            
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        
        return count
