"""
[21-04-18] 100. Same Tree.py
https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q : return True
        if (not p and q) or (not q and p) or (p.val != q.val) : return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
