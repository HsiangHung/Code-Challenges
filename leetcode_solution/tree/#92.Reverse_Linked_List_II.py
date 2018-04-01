# [# 92] Reverse Linked List II
#  
#
#
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n: return head
        
        prev, node, count = None, head, 1
        while node.next != None and count < m:
            nextNode = node.next
            count += 1
            prev= node
            node = nextNode

        # if [1,2,3,4,5] and m=2, n=4, return [4,3,2] 
        # so return reversed_head=4, reversed_tail =2, and prev=1, and left head = 5
        # so prev.next = 4 to connect 1->4, and reversed_tail.next = 5 to connect 2->5
        reversed_head, reversed_tail, nextNode = self.reverseList(node, n-m)
        reversed_tail.next = nextNode
        if not prev:
            return reversed_head

        prev.next = reversed_head
        reversed_tail.next = nextNode
        
        return head
        
        
    def reverseList(self, head, stop_count):
        '''this method is to reverse a linked list with the designed length'''
        count = 0
        prev = None
        node = head
        while node.next != None and count < stop_count:
            nextNode = node.next
            count += 1
            node.next = prev
            prev = node
            node = nextNode
            
        post_list_node = node.next
        node.next = prev
        
        return node, head, post_list_node