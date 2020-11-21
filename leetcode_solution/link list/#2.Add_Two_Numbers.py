# 2 Add Two Numbers (medium)
# https://leetcode.com/problems/add-two-numbers/ 
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
        len_1 = self.getLength(l1)
        len_2 = self.getLength(l2)
        if len_1 >= len_2:
            long_ = l1
            short_ = l2
        else:
            long_ = l2
            short_ = l1
            
        ## at beginning, prepare the head node
        head, next_digit = self.generateNodes(long_, short_, 0)
        node = head
        while short_.next != None:
            long_ = long_.next
            short_ = short_.next
            newNode, next_digit = self.generateNodes(long_, short_, next_digit)
            node.next = newNode
            node = newNode
            
        ## now shorted list has been run over.
        ## next we have to consider like [4,8,8] + [2,6,9] = [6,4,8,1]
        ## also [4,8,8,9,9,9] + [2,6,9] = [6,4,8,0,0,0,1]
        if next_digit == 0:
            if long_.next != None: node.next = long_.next
        else:
            if long_.next == None:
                node.next = ListNode(1)
            else:
                zeroNode = ListNode(0)
                while long_.next != None:
                    long_ = long_.next
                    newNode, next_digit = self.generateNodes(long_, zeroNode, next_digit)
                    node.next = newNode
                    node = newNode
                if next_digit != 0: node.next = ListNode(1)
                    
        return head
        
        
    def generateNodes(self, long_, short_, next_digit):
        """
        :type long_, short_: listNode
        :type next_digit: int
        :rtype: ListNode, int
        """
        sum_ = long_.val + short_.val+next_digit
        next_digit = 0
        if sum_ >= 10: 
            next_digit = 1
            sum_ -= 10
        return ListNode(sum_), next_digit
        
        
    def getLength(self, head):
        """
        get the length of the list
        :type head: ListNode
        :rtype: int
        """
        length = 1
        node = head
        while node.next != None:
            node = node.next
            length += 1
        return length