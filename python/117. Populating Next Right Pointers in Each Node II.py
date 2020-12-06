# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        de = collections.deque([root])
        while de:
            prev = None
            size = len(de)
            for i in range(size):
                curr = de.popleft()
                if prev: prev.next = curr
                if curr and curr.left : de.append(curr.left)
                if curr and curr.right : de.append(curr.right)
                prev = curr
        return root
       
        
