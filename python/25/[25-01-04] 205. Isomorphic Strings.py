"""
[25-01-04] 205. Isomorphic Strings.py
https://leetcode.com/problems/isomorphic-strings
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_to_t = {}
        mapped = set()

        for i in range(len(s)): 

            if s[i] in s_to_t and s_to_t[s[i]] != t[i] : return False
            if s[i] not in s_to_t and t[i] in mapped : return False
            s_to_t[s[i]] = t[i]
            mapped.add(t[i])

        return True
