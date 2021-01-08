"""
[21-01-08] 79. Word Search
https://leetcode.com/problems/word-search/
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, count):
            if count == len(word): return True
            key = str(i) + "_" + str(j)
            if i < 0 or j < 0 or i >= m or j >=n or board[i][j] != word[count]: return False
            temp, board[i][j] = board[i][j], '_'
            re = dfs(i, j + 1, count + 1) or dfs(i+1, j, count + 1) or dfs(i-1, j, count + 1) or  dfs(i, j - 1, count + 1)
            board[i][j] = temp
            return re
            
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen = set()
                    result = dfs(i, j, 0)
                    if result: return True
        return False
        
