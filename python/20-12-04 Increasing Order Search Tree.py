# 897. Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def in_oder(root: TreeNode, in_order_list: List):
            if root is None : return
            in_oder(root.left, in_order_list)
            in_order_list.append(root.val)
            in_oder(root.right, in_order_list)

        in_order_list = []
        in_oder(root, in_order_list)
        
        dummy = TreeNode()
        tail = dummy
        
        for i in in_order_list:
            tail.right = TreeNode(i)
            tail = tail.right
        return dummy.right
