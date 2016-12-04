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
        if head == None or head.next == None: return head
            
        node = head
        prev = None
        while node.next != None:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
            
        node.next = prev
        return node