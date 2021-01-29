"""
[21-01-29] 114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # base case

        
        def flatten_with_leaf(root: TreeNode):
        
            if root is None: return None
            if root.left is None and root.right is None: return root
            left_leaf = flatten_with_leaf(root.left)
            right_leaf = flatten_with_leaf(root.right)
            if left_leaf:
                right = root.right
                root.right = root.left
                left_leaf.right = right
                root.left = None
            
            return right_leaf if right_leaf else left_leaf
        
        flatten_with_leaf(root)
    
