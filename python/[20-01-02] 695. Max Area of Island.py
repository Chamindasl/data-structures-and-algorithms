"""
[20-01-02] 695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0: return 0
            grid[i][j] = 0
            r = dfs(i, j+1)
            l = dfs(i, j-1)
            u = dfs(i-1, j)
            d = dfs(i+1, j)
            return 1 + r + l + u + d

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, dfs(i, j))
                
        return max_area

            
