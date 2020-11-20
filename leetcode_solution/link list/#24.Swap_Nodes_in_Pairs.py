# 24 Swap Nodes in Pairs (medium)
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        new_head = head.next 
        
        prev, node = head, head.next
        while node.next != None and node.next.next != None:
            nextNode = node.next
            nn = nextNode.next
            node.next = prev
            prev.next = nn
            prev, node = nextNode, nn
        
        # now the last prev, node pair doesn't swap. we need to swap them:

        if node.next != None:
            nextNode = node.next  # when odd link-list: [1,2,3,4,5] => [2,1,4,3,5]
            node.next = prev
            prev.next = nextNode
        else:                     # when even link-list: [1,2,3,4]
            node.next = prev
            prev.next = None
            
            
        return new_head