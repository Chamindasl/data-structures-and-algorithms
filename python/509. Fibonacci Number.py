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
            

        
# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        self.cache = {0:0, 1:1}
        
        def memoize(n: int):
            if n in self.cache.keys(): 
                return self.cache[n]
            self.cache[n] = memoize(n-1) + memoize(n-2)
            return self.cache[n]
        
        return memoize(N)
