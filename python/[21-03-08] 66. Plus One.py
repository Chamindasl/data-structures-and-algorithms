"""
66. Plus One.py
https://leetcode.com/problems/plus-one/submissions/
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i]) == 9:
                digits[i] = 0
            else: 
                digits[i] = digits[i] + 1
                return digits
        t = [0] * len(digits)
        return [1] + t
