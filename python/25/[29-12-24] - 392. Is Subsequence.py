"""
[29-12-24] - 392. Is Subsequence.py
https://leetcode.com/problems/is-subsequence
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 : return True
        if len(s) > len(t) : return False

        ps = 0
        pt = 0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        
        return ps == len(s)
        
