"""
[21-01-04] 314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""
class Solution:
    def verticalOrder(self, root: TreeNode, col = 0) -> List[List[int]]:
        
        result = {}
        def dfs(root: TreeNode, row, col):
            if root is None: return
            if col in result:
                result[col].append((row, root.val)) 
            else:
                result[col] = [(row, root.val)]
        
            dfs(root.left, row + 1, col -1)
            dfs(root.right, row + 1 ,  col + 1)
        
        dfs(root, 0, 0)
        f_result = []
        for k, v in sorted(result.items()):
            f_result.append([it[1] for it in sorted(v, key=lambda x: x[0])])
        return f_result
        
        
        
