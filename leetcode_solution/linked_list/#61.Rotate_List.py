# [#61] Rotate List
#
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or head.next == None: return head
        
        length = self.get_length(head)
        
        if k > length: k = k % length
        if k == 0 or k == length: return head
        
        node = head
        expect_length = 1
        while node.next != None:
            nextNode = node.next
            
            if expect_length == length - k:
                head2 = nextNode
                node.next = None
            
            node = nextNode
            expect_length += 1
            
        node.next = head
        
        return head2
            
        
    def get_length(self, head):
        if not head: return 0
        
        node = head
        length = 1
        while node.next != None:
            node = node.next
            length += 1
        
        return length