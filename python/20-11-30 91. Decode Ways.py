# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution:

    def __init__(self):
        self.memo = {}
    
    def numDecodings(self, s: str) -> int:
        return self.rec_numDecodings(s, 0)
        
    def rec_numDecodings(self, s:str, idx):
        # 3 base cases, last idx or last to last or invalid 

        if idx == len(s): 
            return 1
        
        if s[idx] == "0":
            return 0
        
        if idx == len(s) - 1 : 
            return 1
        
        if idx in self.memo:
            return self.memo[idx]
        
        ans = self.rec_numDecodings(s, idx + 1)  + (self.rec_numDecodings(s, idx + 2) if int(s[idx : idx +2]) <=26 else 0)
        
        self.memo[idx] = ans
        
        return ans
        
