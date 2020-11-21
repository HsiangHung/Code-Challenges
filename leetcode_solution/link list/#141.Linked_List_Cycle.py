## 141 Linked List Cycle (easy)
## https://leetcode.com/problems/linked-list-cycle/
##
##  idea: if without additional storage, we can run the linked list in two 
##        different paces, fast = node.next.next and slow = node.next
##        if there is a cycle, then we must have fast = slow; otherwise not.
##
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
            
        return False