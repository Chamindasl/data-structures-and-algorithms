"""
[21-01-04] 1640. Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_dic = {p[0]: p for p in pieces }
        i = 0
        while i < len(arr):
            if arr[i] not in pieces_dic: return False
            for j in pieces_dic[arr[i]]:
                if j != arr[i]: return False
                i += 1
        
        return True
        
