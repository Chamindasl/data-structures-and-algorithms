"""
[28-12-24] 121. Best Time to Buy and Sell Stock.py
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = float('inf')
        p = 0

        for i in prices:
            if b > i :
                b = i
            if p < i - b:
                p = i - b
        return p
        
