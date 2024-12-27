"""
[27-12-24] 88. Merge Sorted Array.py
https://leetcode.com/problems/merge-sorted-array/
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        wp = m + n - 1
        m = m - 1

        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[wp] = nums1[m]
                m = m - 1
            else: 
                nums1[wp] = nums2[n]
                n = n - 1
            wp = wp - 1

        while m >= 0:
            nums1[wp] = nums1[m]
            m = m - 1
            wp = wp - 1

        while n >= 0:
            nums1[wp] = nums2[n]
            n = n - 1
            wp = wp - 1
