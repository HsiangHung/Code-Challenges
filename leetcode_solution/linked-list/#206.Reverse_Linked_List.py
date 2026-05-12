# 206 Reverse Linked List (easy)
# https://leetcode.com/problems/reverse-linked-list/
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if not head: return head
        
        prev, node = None, head
        while node.next != None:
            nextNode = node.next
            
            node.next = prev
            prev = node
            node = nextNode
            
        node.next = prev
        return node