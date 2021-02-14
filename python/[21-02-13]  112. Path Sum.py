"""
[21-01-03] 112. Path Sum
https://leetcode.com/problems/path-sum/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root: TreeNode, sum: int) -> bool:
            if root is not None and root.left is None and root.right is None and sum == root.val: return True
            if root is None: return False
            return helper(root.left, sum - root.val) or helper(root.right, sum - root.val)
        
        return helper(root, sum)
