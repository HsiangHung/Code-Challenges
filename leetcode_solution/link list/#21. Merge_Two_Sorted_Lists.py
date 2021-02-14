#  21 Merge Two Sorted Lists (easy)
#  https://leetcode.com/problems/merge-two-sorted-lists/
#
#  create a list, and moving double pointer
#
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        node = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next 
            
            node = node.next
    
        if not l1: node.next = l2
        if not l2: node.next = l1
            
        return head