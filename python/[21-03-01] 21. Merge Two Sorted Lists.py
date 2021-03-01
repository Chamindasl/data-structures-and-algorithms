"""
[21-03-01] 21. Merge Two Sorted Lists.py
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next
