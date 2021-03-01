"""
[21-03-01] 28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0 
        if not haystack: return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1
