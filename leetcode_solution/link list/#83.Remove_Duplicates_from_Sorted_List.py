## [Leetcode#83] Remove Duplicates from Sorted List
#
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        
        node = head
        while node != None and node.next != None:
            nextNode = node.next
            while nextNode != None and nextNode.val == node.val:
                nextNode = nextNode.next
            node.next = nextNode
            node = nextNode
                
        return head