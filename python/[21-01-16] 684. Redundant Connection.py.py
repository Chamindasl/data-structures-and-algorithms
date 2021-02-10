"""
[21-01-16] 684. Redundant Connection
https://leetcode.com/problems/redundant-connection/
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        seen = set()
        
        graph = collections.defaultdict(set)
        
        def dfs(s, t):
            if s == t : return True
            if s not in seen:
                seen.add(s)
                for news in graph[s]:
                    if dfs(news, t): return True
            return False
        
        for u, v in edges:
            seen.clear()
            if u in graph and v in graph and dfs(u, v): return [u, v]
            graph[u].add(v)
            graph[v].add(u)
