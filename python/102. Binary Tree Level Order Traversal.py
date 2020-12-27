"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            sub = []
            for i in range(size):
                one = queue.pop(0)
                if one:
                    queue.append(one.left)
                    queue.append(one.right)
                    sub.append(one.val)
            if sub:
                result.append(sub)
        return result
