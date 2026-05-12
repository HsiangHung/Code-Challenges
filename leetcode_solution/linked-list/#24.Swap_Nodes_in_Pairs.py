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
        while node and node.next and node.next.next:
            nextNode = node.next
            nn = nextNode.next
            node.next = prev
            prev.next = nn
            prev, node = nextNode, nn
        
        # now the last prev, node pair doesn't swap. we need to swap them:
        if node.next:
            prev.next = node.next
        else:
            prev.next = None
            
        node.next = prev
            
        return new_head