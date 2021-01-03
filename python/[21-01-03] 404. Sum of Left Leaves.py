"""
[21-01-03] 404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(root):
            if root == None : return 
            if root.left and root.left.left is None and root.left.right is None:
                self.sum += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.sum
