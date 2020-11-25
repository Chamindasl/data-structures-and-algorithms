# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx, curr = 0, 0
        for num in nums:
            if num == 0:
                mx = max(mx, curr)
                curr = 0
            else:
                curr += 1
        return max(mx, curr)
