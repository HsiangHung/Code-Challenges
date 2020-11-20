# 19 Remove Nth Node From End of List (medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 
#
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return None
        
        node, length = head, 1
        while node != None:
            if length == n:
                prev, target = None, head
            elif length == n+1:
                prev, target = head, target.next
            elif length > n+1:
                prev, target = prev.next, target.next
            node = node.next
            length += 1
        
        if prev == None:  ## to consider if n == len of linked list
            return head.next
        
        prev.next = target.next
            
        return head
            