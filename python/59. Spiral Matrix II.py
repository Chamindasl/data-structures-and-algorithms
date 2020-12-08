"""
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, right, bottom, left = 0, n - 1, n-1, 0;
        count = 0
        level = 0
        result = [[0]*n for i in range(n)]
        
        while top<=n//2 + n % 2 :
            for i in range(left, right+1, 1):
                count += 1
                result[top][i] = count
            top += 1
            for i in range(top, bottom + 1, 1):
                count += 1
                result[i][right] = count
            right += -1
            for i in range(right, left - 1, -1):
                count += 1
                result[bottom][i] = count
            bottom += -1
            for i in range(bottom, top - 1, -1):
                count += 1
                result[i][left] = count
            left += 1
            
        return result        
