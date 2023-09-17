"""
[23-09-19] 103. Binary Tree Zigzag Level Order Traversal
https://github.com/Chamindasl/data-structures-and-algorithms/new/main/python
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        result = []
        visiting = [root]
        level = -1
        while visiting: 
            level += 1
            sub = []
            size = len(visiting)
            for i in range(size):
                curr = visiting.pop(size - 1  - i)
                if level % 2 == 0:
                    if curr.left: visiting.append(curr.left)
                    if curr.right: visiting.append(curr.right)
                else: 
                    if curr.right: visiting.append(curr.right)
                    if curr.left: visiting.append(curr.left)
                sub.append(curr.val)
            result.append(sub)
        return result
        
