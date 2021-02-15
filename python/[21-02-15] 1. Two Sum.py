# 1. Two Sum
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            if target - num in visited: 
                return visited[target - num], i
            visited[num] = i
        return None
        
