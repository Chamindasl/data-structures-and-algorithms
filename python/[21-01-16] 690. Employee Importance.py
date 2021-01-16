"""
[21-01-16] 690. Employee Importance
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = {e.id: e for e in employees}

        def dfs(idx):
            emp = graph[idx]
            tot = emp.importance
            for subordinate in emp.subordinates:
                tot += dfs(subordinate)
            return tot
        
        return dfs(id)
