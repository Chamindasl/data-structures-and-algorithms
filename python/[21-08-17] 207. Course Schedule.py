"""
[21-08-17] 207. Course Schedule
https://leetcode.com/problems/course-schedule/
"""

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ad = defaultdict(list)
        
        for a, b in prerequisites:
            ad[a].append(b)

        
        def dfs(cou, visited):
            if cou in visited: return False
            if not ad[cou]: return True
            visited.add(cou)
            for pre in ad[cou]:
                if not dfs(pre, visited): return False
            visited.remove(cou)
            ad[cou] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i, set()): return False
        
        return True
