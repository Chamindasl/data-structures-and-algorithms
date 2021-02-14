# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, min_list: ListNode, max_list: ListNode) ->ListNode:
        cf = 0
        dummy = ListNode(0)
        head = dummy
        while min_list is not None or max_list is not None:
            min_val, max_val = 0,0
            if min_list is not None:
                min_val = min_list.val
                min_list = min_list.next
            if max_list is not None:
                max_val = max_list.val
                max_list = max_list.next
            cf, tot = divmod(min_val + max_val + cf,10)
            head.next = ListNode(tot)
            head = head.next
            
        if cf !=0 :
            head.next = ListNode(cf)
        
        return dummy.next
