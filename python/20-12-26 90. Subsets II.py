"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, comb):
            result.append(comb[:])
            for i in range(len(nums)):
                if i == 0 or (nums[i-1] != nums[i]):
                    dfs(nums[i+1:], [nums[i]] + comb)
        
        result = []
        dfs(sorted(nums), [])
        return result
    
