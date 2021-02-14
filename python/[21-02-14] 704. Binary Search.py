# 704. Binary Search
# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = None
        # left mid targt right
        while left <= right : 
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                return mid                
            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        return -1
            
        
