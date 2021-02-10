"""
[21-01-03] 872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        def leafSum(root, leafs):
            if root is None: return
            if root.left is None and root.right == None : leafs.append(root.val)
            leafSum(root.left, leafs)
            leafSum(root.right, leafs)
        leafs1, leafs2 = [], [] 
        leafSum(root1, leafs1)
        leafSum(root2, leafs2) 
        return leafs1 == leafs2
        
