"""
[28-12-04] 28. Find the Index of the First Occurrence in a String.py
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack): return - 1
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                if j == len(needle) - 1: return i
        return -1
