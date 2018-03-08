## [Leetcode#24] Swap Nodes in Pairs
## Given a linked list, swap every two adjacent nodes and return its head.
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
        node = head
        if node == None or node.next == None: return node
        if node.next.next == None:
            nextNode = node.next
            nextNode.next = node
            node.next = None
            return nextNode

        prev= None
        while node.next != None and node.next.next != None:
            nextNode = node.next
            nextNextNode = nextNode.next
            ## -- check head ---
            if head == node: head = nextNode
            ## -- flip--
            if prev != None: prev.next = nextNode
            nextNode.next = node
            node.next =nextNextNode
            prev = node
            ## -- flip is done --
            node = nextNextNode
            
        if node.next != None:
            nextNode = node.next
            prev.next = nextNode
            nextNode.next = node
            node.next = None
        else:
            prev.next = node
            node.next = None
        
        return head