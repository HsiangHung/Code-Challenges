## [leetcode#21] Merge Two Sorted Lists
##
# Definition for singly-linked list.
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
        if l1 == None: return l2
        if l2 == None: return l1
        
        if l1.val < l2.val:
            current = l1
            other = l2
            head = l1
        else:
            current = l2
            other = l1
            head = l2
            
        while current.next != None:
            nextNode = current.next
            if other.val < current.next.val:
                current.next = other
                current = other
                other = nextNode
            else:
                current = nextNode
        
        if other != None: current.next = other
        
        return head
                
                