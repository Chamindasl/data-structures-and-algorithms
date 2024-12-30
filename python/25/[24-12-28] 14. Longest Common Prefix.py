"""
[28-12-24] 14. Longest Common Prefix.py
https://leetcode.com/problems/longest-common-prefix
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0 : return ""

        l = len(strs[0]) 

        for s in strs[1:]:
            if len(s) == 0 : return ""
            for i in range(l):
                if strs[0][i] != s[i] :
                    l = i
                    break
                if i == len(s) - 1:
                    l = len(s)
                    break

        return strs[0][:l]            
