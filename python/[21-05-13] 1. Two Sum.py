"""
[21-05-13] 1. Two Sum
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dic: return [i, num_dic[diff]]
            num_dic[nums[i]] = i
