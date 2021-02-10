# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted (a**2 for a in A)
    
    
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [0]*len(A)
        left = 0
        right = len(A) -1
        result_p = len(A) - 1
        while left<=right:
            left_2 = A[left] ** 2
            right_2 = A[right] ** 2
            if left_2 > right_2:
                result[result_p] = left_2
                left += 1
                result_p -=1
            else: 
                result[result_p] = right_2
                right -= 1
                result_p -=1
        return result
                
