"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        queue = []
        
        queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                one = queue[0]
                if i < size // 2:
                    if one == None and queue[size -2*i -1] != None : return False
                    if one != None and queue[size -2*i -1] == None : return False
                    if one != None and queue[size -2*i -1] != None and one.val != queue[size -2*i -1].val: return False
                one = queue.pop(0)

                if one: 
                    queue.append(one.left)
                    queue.append(one.right)
        return True
        
