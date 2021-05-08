#  445. Add Two Numbers II (medium)
#  https://leetcode.com/problems/add-two-numbers-ii/
#
# Definition for singly-linked list.
#     def __init__(self, val=0, nodenext=None):
#         self.val = valprev.next = 
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1: 
            return l2
        elif not l2:
            return l1
        
        r1 = self.reverse_linkedlist(l1)
        r2 = self.reverse_linkedlist(l2)
        
        prev, nextdigit = None, 0
        head = None
        while r1 and r2:
            val = r1.val + r2.val + nextdigit
            nextdigit = val // 10
            node = ListNode(val = val % 10)
            
            if not head:
                head = node
            
            if prev:
                prev.next = node
                
            prev = node
            r1 = r1.next 
            r2 = r2.next

        if r1:
            r = r1
        else:
            r = r2
        
        while r:
            val = r.val + nextdigit
            nextdigit = val // 10
            node = ListNode(val = val % 10 )
            prev.next = node
            prev = node
            r = r.next
            
        if nextdigit != 0:
            node = ListNode(val = nextdigit)
            prev.next = node
            
        return self.reverse_linkedlist(head)
        
    def reverse_linkedlist(self, l):
        if not l: return 
        prev, node = None, l
        while node.next:
            nextNode = node.next
            node.next = prev 
            prev = node
            node = nextNode
        node.next = prev
        return node
