"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
            
        
