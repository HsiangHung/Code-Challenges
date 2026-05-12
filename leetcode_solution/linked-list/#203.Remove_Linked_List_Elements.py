# 203 Remove Linked List Elements (easy)
# https://leetcode.com/problems/remove-linked-list-elements/ 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        
        while head.val == val:
            head = head.next
            if not head: return None
        
        node = head
        while node.next:
            nextNode = node.next
            if nextNode.val == val:
                node.next = nextNode.next
                if not nextNode.next: break
            else:
                node = nextNode
        
        return head