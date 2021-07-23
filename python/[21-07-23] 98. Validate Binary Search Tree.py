"""
[21-07-23] 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def validate(root, mini, maxi):
            if not root: return True
            
            if root.val<= mini or root.val >= maxi: return False
            
            return validate(root.left, mini, root.val) and validate(root.right, root.val, maxi)
        
        return validate(root, float("-inf"), float("inf"))
