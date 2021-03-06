# 328 Odd Even Linked List (medium)
# https://leetcode.com/problems/odd-even-linked-list/
#
# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
#  key idea: during propagate, change next to nextnext node, then odd-odd-odd-.. and even-even-even-...
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None or head.next.next == None: return head
        
        odd, even = head, head.next
        odd_head, even_head = odd, even
        
        node, nextNode, nextNextNode = head, head.next, head.next.next
        pos = 0
        while nextNode != None and nextNextNode != None:
            pos += 1
            if pos % 2 == 1:
                odd.next = nextNextNode
                odd = odd.next
            else:
                even.next = nextNextNode
                even = even.next
            
            node = nextNode
            nextNode = nextNextNode
            nextNextNode = nextNextNode.next
                  
        even.next = None
        odd.next = even_head
        
        return odd_head