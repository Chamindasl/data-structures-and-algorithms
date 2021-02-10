"""
[21-01-17] 199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        q = [root]
        result = []
        while q:
            size= len(q)
            for i in range(size):
                node = q.pop(0)
                if node: 
                    if node.left: q.append(node.left) 
                    if node.right: q.append(node.right)
                    if i == size - 1: result.append(node.val)
        return result
