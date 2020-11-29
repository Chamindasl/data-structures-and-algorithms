# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p3 = m - 1, n -1, m + n -1
        
        while p3>=0:
            num1 = -float(inf) if p1 < 0 else nums1[p1]
            num2 = -float(inf) if p2 < 0 else nums2[p2]
            if num1>num2:
                nums1[p3] = num1
                p1 += -1
                p3 += -1
            else: 
                nums1[p3] = num2
                p2 += -1
                p3 += -1
        
            
