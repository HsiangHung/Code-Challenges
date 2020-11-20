# 83 Remove Duplicates from Sorted List (easy)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
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


## solution 2: if duplication, skip the current node and let prev.next = next node
class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None: return head
        
        prev, node = None, head
        while node.next != None:
            nextNode = node.next
            if nextNode.val == node.val:
                if node != head:
                    node = nextNode
                    prev.next = node
                else:
                    node = nextNode
                    head = node
            else:
                prev= node
                node = nextNode
                
        return head