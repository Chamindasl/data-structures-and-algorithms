"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        curr_sum = 0
        sign = 1 if x >= 0 else -1
        x*=sign
        while x:
            x, m = divmod(x,10)
            curr_sum = curr_sum * 10 + m
        re = sign * curr_sum
        return re if abs(re)< math.pow(2,31) else 0
        
