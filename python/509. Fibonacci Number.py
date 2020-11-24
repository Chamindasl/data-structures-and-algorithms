# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1: 
            return 1
        prev = 1
        prev_prev = 0
        for _ in range(2, N+1):
            temp = prev
            prev = prev + prev_prev
            prev_prev = temp
            
        return prev            
            
