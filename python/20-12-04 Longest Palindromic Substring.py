# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub = ""
        
        def expand_to_sides(s, i, j):
            while i>=0 and j < len(s):
                if s[i] != s[j] : return s[i+1:j]
                i-=1
                j+=1
            return s[i+1:j]
        
        for i in range(len(s)):
            this_max_sub = expand_to_sides(s, i, i)
            longest_sub = this_max_sub if len(longest_sub) < len(this_max_sub) else longest_sub
            
        for i in range(len(s) -1):
            if (s[i] == s[i+1]):
                this_max_sub = expand_to_sides(s, i, i+1)
                longest_sub = this_max_sub if len(longest_sub) < len(this_max_sub) else longest_sub
        
        return longest_sub
