"""
67. Add Binary.py
https://leetcode.com/problems/add-binary/
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        cf = 0
        re = ''
        for i in range(max(len(a), len(b))):
            ai = len(a) - 1 - i
            bi = len(b) - 1 - i
            ta = 1 if ai >=0 and a[ai] == '1' else 0
            tb = 1 if bi >=0 and b[bi] == '1' else 0
            
            cf, br = divmod(ta + tb + cf, 2)
            
            re = str(br) + re
        
        if cf : re = '1' + re
        return re
