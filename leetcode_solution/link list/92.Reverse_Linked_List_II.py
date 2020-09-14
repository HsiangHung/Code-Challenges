# #92. Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n: return head
        
        node, i = head, 1
        while node != None and node.next != None:
            
            if m == 1:
                r_head, tailNext = self.reverse_linked_list(0, n, node) 
                node = tailNext
                if node != None:
                    node = node.next
                break
            elif m != 1 and i == m-1:
                before_reverse = node
                r_head, tailNext = self.reverse_linked_list(i, n, node.next)
                before_reverse.next = r_head 
                node = tailNext
                if node != None:
                    node = node.next
                i += 1
            else:
                node = node.next
                i += 1
        
        if m == 1:
            return r_head
        else:
            return head
            
        
    def reverse_linked_list(self, len, m, head):
        prev, node, nextNode = None, head, head.next
        len += 1
        while nextNode != None and len < m:
            node.next = prev
            prev = node
            node = nextNode
            nextNode = node.next
            len += 1

        nextNode = node.next # get the node after the head: e.g. 5
        node.next = prev     # 4 -> 3
        head.next = nextNode  # 2 -> 5
        return node, nextNode # return head, and node after tail of the reverse linked list