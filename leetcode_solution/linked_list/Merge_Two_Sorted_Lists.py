## [Leetcode#21] Merge Two Sorted Lists
## Merge two sorted linked lists and return it as a new list. The new list should be made by splicing 
##together the nodes of the first two lists.
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        if l1 == None: return l2
        if l2 == None: return l1
        
        if l1.val < l2.val:
            head = l1
            node = head
            other = l2
        else:
            head = l2
            node = head
            other = l1
            
        while node.next != None:
            nextNode = node.next
            nextval = nextNode.val
            otherval = other.val
            if nextval <= otherval:
                node = node.next
            else:
                node.next = other
                other = nextNode
                node = node.next
            
        node.next = other
        
        return head

