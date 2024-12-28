"""
[28-12-24] 58. Length of Last Word.py
https://leetcode.com/problems/length-of-last-word/
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        started = False
        length = 0

        for i in range(len(s) - 1, -1, -1):
            c = s[i] 
            if c != ' ' :
                started = True

            if started and c != ' ' : 
                length += 1
            elif started : break

        return length
