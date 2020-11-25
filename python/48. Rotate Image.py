# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) -1
        for level in range((size + 1)//2):
            for x in range(level, size - level):
                temp = matrix[x][size-level]
                matrix[x][size-level] = matrix[level][x]
                matrix[level][x] = matrix[size - x][level]
                matrix[size - x][level] = matrix[size - level][size - x]
                matrix[size - level][size - x] = temp
                           
        
