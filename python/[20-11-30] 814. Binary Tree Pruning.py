# 814. Binary Tree Pruning
# https://leetcode.com/problems/binary-tree-pruning/solution/
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def hasOne(root: TreeNode):
            if not root: return False
            left_ones = hasOne(root.left)
            right_ones = hasOne(root.right)
            if not left_ones: root.left = None
            if not right_ones: root.right = None
            return root.val == 1 or left_ones or right_ones
            
        return root if hasOne(root) else None
        
