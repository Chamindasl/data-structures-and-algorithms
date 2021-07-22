"""
[21-07-22] 783. Minimum Distance Between BST Nodes.py
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        ans = []
        
        def dfs(node):
            if node:
                ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        ans.sort()
        mini = float('inf')
        for i in range(len(ans) - 1):
            mini = min(mini, ans[i+1] - ans[i])
        return mini
