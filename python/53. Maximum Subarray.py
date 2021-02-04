"""
[21-02-04] - 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = -float(inf), 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], nums[i] + curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max(max_sum, curr_sum)
