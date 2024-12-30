"""
[30-12-24] - 383. Ransom Note.py
https://leetcode.com/problems/ransom-note
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran_hm = {}

        for c in ransomNote:
            ran_hm[c] = 1 + ran_hm.get(c, 0)

        for c in magazine:
            if c in ran_hm:
                ran_hm[c] = ran_hm.get(c) - 1
                if ran_hm[c] == 0 : ran_hm.pop(c)

        if ran_hm : return False

        return True
