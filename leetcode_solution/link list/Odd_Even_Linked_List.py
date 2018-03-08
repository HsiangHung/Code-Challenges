## [Leetcode#328] Odd Even Linked List
## Given a singly linked list, group all odd nodes together followed by the even nodes. 
## Please note here we are talking about the node number and not the value in the nodes.
##
##  key idea: during propagate, change next to nextnext node, then odd-odd-odd-.. and even-even-even-...
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        if head.next.next == None: return head
        
        evenHead = head.next
        
        node = head
        prev = None
        index =1
        while node.next != None:
            nextNode = node.next
            if prev != None: prev.next = nextNode
            prev = node
            node = nextNode
            index += 1
            
        if index %2 ==1: 
            node.next = evenHead
            prev.next = None
        elif index %2 ==0: 
            prev.next = evenHead
        
        return head

