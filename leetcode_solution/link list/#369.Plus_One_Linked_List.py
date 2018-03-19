# [#369] Plus One Linked List
#
#  reverse first, and add one and reverse again
#  need to consider extreme case 9->9->9 + 1 = 1->0->0->0
#
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        
        head = self.reverse_list(head)
        add_one_head = self.add_one(head)
        return self.reverse_list(add_one_head)
            
        
    def add_one(self, head):
        if not head: return ListNode(1)
        
        node = head
        node.val += 1
        while node.val == 10 and node.next != None:
            nextNode = node.next
            node.val = 0
            node = nextNode
            node.val += 1
            
        if node.val == 10:
            node.val = 0
            node.next = ListNode(1)
            
        return head
                
                
    def reverse_list(self, head):
        '''reverse a linked list'''
        if not head: return None
        if head.next == None: return head
        
        prev = None
        node = head
        while node.next != None:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
    
        node.next = prev
        return node