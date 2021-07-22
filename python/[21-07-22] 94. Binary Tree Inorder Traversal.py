"""
[21-07-22] 94. Binary Tree Inorder Traversal.py
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def inIte():
       
            if not root: return []

            ans = []
            stack = []
            stack.append(root)
            curr = root

            while stack:
                if curr: 
                    stack.append(curr)
                    curr = curr.left
                else: 
                    curr = stack.pop()
                    ans.append(curr.val)
                    curr = curr.right
            ans.pop()
            return ans
        
        def inReq(root, ans):
            if root:
                inReq(root.left, ans)
                ans.append(root.val)
                inReq(root.right, ans)

        ans = []
        inReq(root, ans)
        return ans

#        return inIte()
