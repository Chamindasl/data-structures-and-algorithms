# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]<nums[-1]:
            return self.binarySearch(nums, target, 0, len(nums) - 1)
        else: 
            rotate_index_ = self.rotate_index(nums)
            first_half = self.binarySearch(nums, target, 0, rotate_index_ - 1)
            if first_half != -1: 
                return first_half
            else: 
                return self.binarySearch(nums, target, rotate_index_, len(nums) - 1)
    
    def rotate_index(self, nums) ->int:
        if len(nums) <= 1:
            return 0
        left, right = 0, len(nums) -1
        mid = right // 2
        # left   mid rotation right
        while nums[mid]<nums[mid+1]:
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
            mid = left + (right - left) // 2
        return mid+1
    
    
    
    def binarySearch(self, nums, target, left, right):
        while left<=right:
            mid = left + (right - left) // 2
            # left mid target right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid -1
        return -1
