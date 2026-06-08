#
# 876. Middle of the Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Run two linked-lists in parallel:
         linked-list 1 move normally, every node
         linked-list 2 only move to next node when list 1 move two nodes
        """

        if not head or not head.next:
            return head

        l1 = head
        l2 = head

        i = 0
        while l1.next:
            l1 = l1.next
            if i % 2 == 0:
                l2 = l2.next
            i += 1

        return l2
