## 160 Intersection of Two Linked Lists (easy)
## https://leetcode.com/problems/intersection-of-two-linked-lists/
##
##  doing short + long and long + short, there will be same node if merge
##  otherwise return None
##
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        
        if self.get_length(headA) >= self.get_length(headB):
            long, long_head, short, short_head = headA, headA, headB, headB
        else:
            long, long_head, short, short_head = headB, headB, headA, headA
            
        while short != None:
            if long.val == short.val: return long
            long = long.next
            short = short.next

        if long == None: return None
        short = long_head
        while long != None:
            if long.val == short.val: return long
            long = long.next
            short = short.next
            
        if short == None: return None
        long = short_head
        while short != None:
            if long.val == short.val: return long
            long = long.next
            short = short.next
            
        return None
        
    
    def get_length(self, head):
        if not head: return 0
        length, node = 1, head
        while node.next != None:
            length += 1
            node = node.next
        return length