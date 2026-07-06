# 92. Reverse Linked List II (medium)
# https://leetcode.com/problems/reverse-linked-list-ii/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        prev, curr = None, head
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        normal_tail, reverse_tail = prev, curr

        # ------ reverse linked list ---------
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # ------ reverse linked list ---------
        
        if normal_tail:
            normal_tail.next = prev
        else:
            head = prev
    
        reverse_tail.next = curr

        return head
