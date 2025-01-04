"""
[25-01-04] - 242. Valid Anagram.py
https://leetcode.com/problems/valid-anagram
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        wc = {}

        for i in range(len(s)):
            wc[s[i]] = wc.get(s[i], 0 ) + 1
            wc[t[i]] = wc.get(t[i], 0 ) - 1
        
        for c, cc in wc.items():
            if cc != 0: return False

        return True

