"""
46. Permutations
https://leetcode.com/problems/permutations/
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def dfs(nums, comb, count):
            if count == 0:
                result.append(comb[:])
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], [nums[i]] + comb, count - 1)
        
        dfs(nums, [], len(nums))
        
        return result
                
        
