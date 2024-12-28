"""
[27-12-24] 27. Remove Element.py
https://leetcode.com/problems/remove-element
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j


