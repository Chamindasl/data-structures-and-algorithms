"""
77. Combinations
https://leetcode.com/problems/combinations/
"""
class Solution:
    def combine(self, n: int, k: int, s=1) -> List[List[int]]:
        if k == 0: return [[]]
        result = []
        for i in range(s, n + 1):
            com = [[i] + one for one in self.combine(n, k-1, i+1)]
            result+=com
        return result
            
        
