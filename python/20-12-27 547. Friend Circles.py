"""
547. Friend Circles
https://leetcode.com/problems/friend-circles/
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        def dfs(m, visited, row):
            for col in range(len(m)):
                if m[row][col] == 1 and col not in visited: 
                    visited.add(col)
                    dfs(m, visited, col)
        
        count = 0
        visited = set()
        for row in range(len(M)):
            if row not in visited:
                count+=1
                dfs(M, visited, row)
        return count
        
