# # 143. Reorder List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        e.g. 1->2->3->4->5->6
        trick: first half normal, 1->2->3 ,
               second reverse,    6->5->4
               then zig-zag it 1->6->2->5->3->4
               
        NOTE: if len is odd, like 1->2->3->4->5
        
        '''
        if not head or not head.next: return head
        
        list_len = self.get_length(head)
        half_len = int((list_len+1)/2)
        
        len = 1
        node = head
        while len <= half_len:
            node = node.next
            len += 1
        
        reverse_head = self.get_reverse_link(node)
        
        node, node2 = head, reverse_head
        while node2.next != None:
            nextNode  = node.next
            nextNode2 = node2.next
            
            node.next = node2
            node2.next = nextNode
            
            node  = nextNode
            node2 = nextNode2
            
        if list_len % 2 == 1: # the last part is tricky part. 
            nextNode  = node.next
            node.next = node2
            node2.next = nextNode
            nextNode.next = None
        
        
    def get_reverse_link(self, head):
        
        if not head or not head.next: return head
        
        prev, node, nextNode = None, head, head.next
        while nextNode != None:
            node.next = prev
            
            prev = node
            node = nextNode
            nextNode = node.next
            
        node.next = prev
        
        return node
            
        
    def get_length(self, node):
        len = 1
        while node.next != None:
            node = node.next
            len += 1
        return len