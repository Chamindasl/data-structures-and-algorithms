"""
[21-17-21] 1089. Duplicate Zeros.py
https://leetcode.com/problems/duplicate-zeros/
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zero_idx = -1
        idx = -1
        for i in range(len(arr)):
            zero_idx += 1
            idx += 1
            if arr[i] == 0:
                zero_idx += 1
            
            if zero_idx >= len(arr) -1 :
                break
            
        if zero_idx > len(arr) - 1:
            arr[len(arr) - 1] = 0
            idx -= 1
            zero_idx = len(arr) - 2
            
        for i in range(idx, -1, -1):
            arr[zero_idx] = arr[i]
            zero_idx -= 1
            if arr[i] == 0:
                arr[zero_idx] = 0
                zero_idx -= 1           
