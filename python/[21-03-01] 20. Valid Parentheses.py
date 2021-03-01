"""
https://leetcode.com/problems/valid-parentheses/
[21-03-01] 20. Valid Parentheses.py
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {')':'(', '}': '{', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] not in brackets:
                stack.append(s[i])
            else: 
                if not stack or  stack.pop() != brackets[s[i]]: return False
        
        return len(stack)==0
