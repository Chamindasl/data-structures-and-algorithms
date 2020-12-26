"""
78. Subsets
https://leetcode.com/problems/subsets/
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, comb):
            result.append(comb[:])
            for i in range(len(nums)):
                dfs(nums[i+1:], comb + [nums[i]])
        
        result = []
        dfs(nums, [])
        
        def pyway(nums):
            result = [[]]
            for num in nums:
                result += [[num] + one for one in result]
            return result        
        
        return result
#        return pyway(nums)
        
