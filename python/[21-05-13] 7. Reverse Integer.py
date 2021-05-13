"""
[21-05-13] 7. Reverse Integer.py
https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        lim = pow(2,31)
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x and rev < lim: 
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
        if (sign == -1 and rev >= lim) or (sign == 1 and rev >= (lim - 1)) : return 0
        return rev * sign
