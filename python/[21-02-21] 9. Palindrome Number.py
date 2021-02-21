"""
[21-02-21] 9. Palindrome Number.py
https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        if x % 10 == 0: return False
        tmp_x = x
        rev_x = 0
        
        while tmp_x > rev_x:
            tmp_x, m = divmod(tmp_x, 10)
            rev_x = rev_x * 10 + m
            
        return rev_x == tmp_x or rev_x // 10 == tmp_x
