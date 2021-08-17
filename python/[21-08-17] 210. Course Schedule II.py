"""
[21-08-17] 210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
"""
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(set)
        
        for c, p in prerequisites:
            adj[c].add(p)
            
        
        # visiting, visited, 
        
        order = []
        visited = set()
        
        def dfs(c, v):
            if c in v: return False
            if c in visited: return True
            v.add(c)
            for p in adj[c]:
                if not dfs(p, v): return False
            v.remove(c)
            visited.add(c)
            order.append(c)
            return True
        
        for i in range(numCourses):
            visiting= set()
            if not dfs(i, visiting): return []
        
        return order                           
