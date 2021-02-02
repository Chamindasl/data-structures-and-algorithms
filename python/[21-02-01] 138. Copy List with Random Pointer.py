"""
[21-02-01] 138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        old_to_new = {}
        
        new_head = Node(0)
        new_tail = new_head
        
        while head:
            copy = Node(head.val)
            new_tail.next = copy
            old_to_new[head] = copy
            new_tail = copy
            head = head.next
        for old in old_to_new:
            if old and old.random:
                old_to_new[old].random = old_to_new[old.random]
        
        return new_head.next
            
        
        
