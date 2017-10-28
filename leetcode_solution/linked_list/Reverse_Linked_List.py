## [Leetcode#206] Reverse Linked List
##
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
        if not head or not head.next: return head
        
        prev = None
        node = head
        nextNode = node.next
        while node.next:
            node.next = prev
            prev = node
            node = nextNode
            nextNode = node.next
            
        node.next = prev
        return node