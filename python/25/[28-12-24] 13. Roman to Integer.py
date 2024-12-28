"""
[28-12-24] 13. Roman to Integer.py
https://leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:

        symToValMap = {
            'I'      :       1,
            'V'      :       5,
            'X'      :       10,
            'L'      :       50,
            'C'      :       100,
            'D'      :       500,
            'M'      :       1000,            
        }
        
        result = symToValMap[s[0]]

        for i in range(1, len(s)):
            result = result + symToValMap[s[i]]
            if symToValMap[s[i-1]] < symToValMap[s[i]]:
                result = result - 2 * symToValMap[s[i-1]]
        
        return result
            
