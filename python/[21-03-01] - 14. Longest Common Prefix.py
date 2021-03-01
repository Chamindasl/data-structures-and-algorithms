"""
[21-03-01] - 14. Longest Common Prefix.py
https://leetcode.com/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]: return ""
        idx = 0
        while idx < len(strs[0]):
            for m in range(1, len(strs)):
                if idx >= len(strs[m]) or strs[0][idx] != strs[m][idx]:
                    return strs[0][:idx]
            idx+=1
        return strs[0]        
