"""
[21-01-04] 107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        queue = []
        re = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            sub = []
            for i in range(size):
                one = queue.pop(0)
                if one: 
                    sub.append(one.val)
                    queue.append(one.left)
                    queue.append(one.right)
            if sub:
                re.append(sub)
        
        return re[::-1]
                
