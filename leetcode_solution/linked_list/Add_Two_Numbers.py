## [Leetcode#2] Add Two Numbers
# 
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.next == None and l2.next == None:
            head, num = self.new_node(l1.val + l2.val)
            if num == 1: head.next = ListNode(1)
            return head
        
        head, num = self.new_node(l1.val + l2.val)
        node = head
        node1 = l1
        node2 = l2
        while node1.next != None and node2.next != None:
            newNode, num = self.new_node(node1.next.val + node2.next.val + num)
            node.next = newNode
            node = newNode
            node1 = node1.next
            node2 = node2.next
        #print node1.val, node2.val
            
        # --------------------------
        if node2.next != None: node1 = node2
        
        while node1.next != None:
            newNode, num = self.new_node(node1.next.val + num)
            node.next = newNode
            node = newNode
            node1 = node1.next
    
        ## this considers [3,2,9,9,9] + [5,9,1] = [8,1,1,0,0,0,1], additional digits
        if num == 1: newNode.next = ListNode(1)
        
        return head


    def new_node(self, sum):
        if sum >= 10:
            newNode = ListNode(sum-10)
            num = 1
        else:
            newNode = ListNode(sum)
            num = 0
        return newNode, num
        