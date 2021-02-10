"""
[21-01-03] 257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        result = []
        def dfs(root, st):
            if root is None: return
            if root is not None and root.left is None and root.right is None: 
                result.append(st + str(root.val))
                return
            dfs(root.left, st + str(root.val) + "->")
            dfs(root.right, st + str(root.val) + "->")
        
        dfs(root, "")
        return result
                
        
        
