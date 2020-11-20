# 92. Reverse Linked List II (medium)
# https://leetcode.com/problems/reverse-linked-list-ii/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        here we separate two cases for reverse: if m = 1 or m > 1
        (1) if m = 1, we return the reverse head, 
            and reverse.next = next node of reverse head
        (2) if m > 1, we return original head.
        '''
        if not head or m == n: return head
        
        if m > 1:
            node1, currLen = head, 1
            while node1.next != None and currLen < m-1:
                node1 = node1.next
                currLen +=1
            rnext, rhead, rtail = self.reverse(m, n, node1.next)
            node1.next = rhead
            rtail.next = rnext
            return head
        elif m == 1:
            rnext, rhead, rtail = self.reverse(m, n, head)
            rtail.next = rnext
            return rhead
        
        
    def reverse(self, Len, n, node):
        if not node or not node.next: return node, node
        
        head = node        
        prev, node = None, node
        while node.next != None and Len < n:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
            Len += 1
        
        nextNode = node.next
        node.next = prev
        return nextNode, node, head 