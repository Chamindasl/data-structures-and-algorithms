"""
[21-01-03] 733. Flood Fill.py
https://leetcode.com/problems/flood-fill/submissions/
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        start_color = image[sr][sc]
        
        def dfs(i, j):
            if i < 0 or i >= len(image) or j < 0 or j >=len(image[0]): return
            if image[i][j] == start_color:
                image[i][j] = newColor
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        if start_color != newColor:
            dfs(sr, sc)
        
        return image
