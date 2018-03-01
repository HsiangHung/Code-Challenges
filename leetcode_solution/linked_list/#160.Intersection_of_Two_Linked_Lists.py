## [Leetcode#160] Intersection of Two Linked Lists
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
        if headA == None or headB == None: return None
        
        if headA.val == headB.val: return headA
        
        len_A = self.getLength(headA)
        len_B = self.getLength(headB)
        diff_len = abs(len_A - len_B)
        if len_A == len_B:
            nodeA = headA
            nodeB = headB
            while nodeA != None and nodeB != None:
                if nodeA.val == nodeB.val: return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next
            return None
        elif len_A != len_B:
            if len_A > len_B:
                long_  = headA
                short_ = headB
            else:
                long_  = headB
                short_ = headA
                
            #print long_.val, short_.val, diff_len
            length = 0
            while long_.next != None:
                length += 1
                long_ = long_.next
                if length == diff_len: break
            #print long_.val
            while long_.next != None and short_.next != None:
                if long_.val == short_.val: return short_
                long_ = long_.next
                short_ = short_.next
            if long_.val == short_.val: return short_

            return None
        
        
    def getLength(self, head):
        """
        get length of a linked list
        : type head: ListNode
        : rtype: int
        """
        if head == None: return 0
        length = 0
        node = head
        while node.next != None:
            length += 1
            node = node.next
        return length +1