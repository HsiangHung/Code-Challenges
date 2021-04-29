#  2. Add Two Numbers (medium)
#  https://leetcode.com/problems/add-two-numbers/ 
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2: return None      
        
        head, prev, nextdigit = None, None, 0
        while l1 and l2:
            listsum = l1.val + l2.val + nextdigit
            node, nextdigit = ListNode(val = listsum % 10), listsum // 10
            
            if not head:
                head = node
            else:
                prev.next = node
                
            prev = node
            l1 = l1.next
            l2 = l2.next
        
        if not l1 and not l2:
            remain = None
        elif l1:
            remain = l1
        elif l2:
            remain = l2
        
        while remain:
            listsum = remain.val + nextdigit
            node, nextdigit = ListNode(val = listsum % 10), listsum // 10
            prev.next = node
            prev = node
            remain = remain.next
        
        if nextdigit == 1:
            prev.next = ListNode(val=1)
        
        return head