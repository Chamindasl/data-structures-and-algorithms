"""
[21-02-10] - 145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root : return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
