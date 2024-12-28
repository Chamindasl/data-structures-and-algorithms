"""
[27-12-24] 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 1
        p = 0
        for i in range (1, len(nums)):
            if nums[p] != nums[i]:
                p = p + 1
                nums[p] =  nums[i]
                result = result + 1
        return result
