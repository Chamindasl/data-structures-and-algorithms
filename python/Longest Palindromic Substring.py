# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palin=""
        
        for i in range(len(s)):
            j = 1
            while(i - j >= 0 and i + j <len(s)) :
                if s[i-j] != s [i+j]:
                    longest_palin = max(longest_palin, s[i-j+1: i+j], key=lambda x:len(x))
                    break
                j +=1

            longest_palin = max(longest_palin, s[i-j+1: i+j], key=lambda x:len(x))
                
        for i in range(len(s) - 1):
            if s[i]==s[i+1]:
                j = 1
                while(i - j >= 0 and i + j + 1<len(s)) :
                    if s[i-j] != s [i+j+1]:
                        longest_palin = max(longest_palin, s[i-j+1: i+j+1], key=lambda x:len(x))
                        break
                    j +=1
                longest_palin = max(longest_palin, s[i-j+1: i+j+1], key=lambda x:len(x))
        return longest_palin
        
