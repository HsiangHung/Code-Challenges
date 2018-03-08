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
        
        prev = None
        node = head
        while node.next != None:
            nextNode = node.next
            if nextNode.val == node.val:
                if prev != None:
                    prev.next = nextNode
                else:
                    head = nextNode
            else:
                prev = node
                
            node = nextNode
            
        return head

