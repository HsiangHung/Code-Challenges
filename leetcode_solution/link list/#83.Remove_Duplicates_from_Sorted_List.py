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
        while node.next != None:
            nextNode = node.next
            if nextNode.val == node.val:
                if nextNode.next != None:
                    node.next = nextNode.next
                else:
                    node.next = None
            else:
                node = nextNode
                
        return head