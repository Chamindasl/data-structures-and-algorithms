"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs_mark_unwanted(x, y, ox, oy):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) : return
            curr =  board[x][y]
            if curr == 'U' or curr == 'X' : return
            board[x][y] = 'U'
            dfs_mark_unwanted(x-1, y, x, y)
            dfs_mark_unwanted(x+1, y, x,y )
            dfs_mark_unwanted(x, y+1, x, y)
            dfs_mark_unwanted(x, y-1, x, y)
        if board:
            for i in range(len(board[0])):
                dfs_mark_unwanted(0, i, 0, i)
                dfs_mark_unwanted(len(board) - 1, i, len(board) - 1, i)
            for j in range(len(board)):
                dfs_mark_unwanted(j, 0, j, 0)
                dfs_mark_unwanted(j, len(board[0]) - 1, j, len(board[0]) - 1)

            for j in range(0, len(board[0])):
                for i in range(0, len(board)):
                    if board[i][j] == 'O': board[i][j] = 'X'
                    if board[i][j] == 'U': board[i][j] = 'O'
        
