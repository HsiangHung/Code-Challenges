# 328 Odd Even Linked List (medium)
# https://leetcode.com/problems/odd-even-linked-list/
#
# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
#  key idea: during propagate, change next to nextnext node, then odd-odd-odd-.. and even-even-even-...
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None or head.next.next == None: return head
        
        odd, even = head, head.next
        odd_head, even_head = odd, even
        
        curr = even.next
        while curr and curr.next:
            # curr is always odd node
            next_curr = curr.next

            odd.next = curr
            even.next = next_curr

            odd = odd.next
            even = even.next

            curr = next_curr.next

        if curr:
            odd.next = curr
            odd = odd.next

        odd.next = even_head
        even.next = None
        return odd_head
