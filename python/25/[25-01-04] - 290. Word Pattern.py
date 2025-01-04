"""
[25-01-04] - 290. Word Pattern.py
https://leetcode.com/problems/word-pattern
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s = {}
        mapped = set()

        words = s.split()

        if len(words) != len(pattern): return False

        for i in range(len(pattern)):

            if pattern[i] in p_to_s and p_to_s[pattern[i]] != words[i] : return False
            elif pattern[i] not in p_to_s and words[i] in mapped: return False
            else:
                p_to_s[pattern[i]] = words[i]
                mapped.add(words[i])
        
        return True
        
