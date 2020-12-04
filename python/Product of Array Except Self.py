# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_left_prod, to_right_prod = [1] * len(nums), [1] * len(nums)
        
        for i in range (1, len(nums)):
            to_left_prod[i] = to_left_prod[i-1] * nums[i-1] 
            to_right_prod[-i - 1] = to_right_prod[-i - 1 +1] * nums[-i - 1 +1]
        
        return [to_left_prod[i] * to_right_prod[i] for i in range(len(nums))]
