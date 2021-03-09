"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        left = len(s) - 1
        while left>=0:
            if not s[left] == ' ' : break
            left -= 1
        
        right = left
        
        while right>=0:
            if s[right] == ' ':
                return left - right
            right -= 1
        return left - right
