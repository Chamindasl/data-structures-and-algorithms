# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        left = self.isPalindrome(s, left, right)
        if left == -1: 
            return True
        else:
            return self.isPalindrome(s, left, right-left-1) == -1 or self.isPalindrome(s, left+1, right-left) == -1
    
    def isPalindrome(self, s, left, right) -> int:
        while left<=right:
            if s[left] == s[right] :
                left += 1
                right -= 1
            else:
                return left;
        return -1
