"""
[25-01-04] - 1. Two Sum.py
https://leetcode.com/problems/two-sum
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visi = {}

        for i, n in enumerate(nums):
            if target - n in visi: return [i, visi[target - n]]
            visi[n] = i
        
        return None
        # visited = {}
        # for i, n in enumerate(nums):
        #     if target - n in visited:
        #         return visited[target - n], i
        #     visited[n] = i
        # return None
        
