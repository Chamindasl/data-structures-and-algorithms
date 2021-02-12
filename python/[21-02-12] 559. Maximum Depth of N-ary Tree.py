"""
[21-01-04] 559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(root):
            if root is None: return 0
            max_d = 0
            for c in root.children:
                max_d = max(max_d, dfs(c))
            
            return max_d + 1
        
        return dfs(root)
