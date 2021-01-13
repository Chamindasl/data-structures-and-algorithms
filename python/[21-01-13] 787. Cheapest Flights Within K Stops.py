"""
[21-01-13] 787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        matrix = [[0] * n for _ in range(n)]

        for flight in flights:
            matrix[flight[0]][flight[1]] = flight[2]
        
        heap = [(0, 0, src)]
        
        while heap:
            cost, hops, port = heapq.heappop(heap)
            if port == dst and hops <= K + 1: return cost
            if hops > K + 1: continue
            
            for i in range(n):
                if matrix[port][i] > 0:
                    heapq.heappush(heap, (cost + matrix[port][i], hops + 1, i))
        return -1
