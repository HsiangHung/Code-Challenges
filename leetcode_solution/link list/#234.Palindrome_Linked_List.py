## [Leetcode#234] Palindrome Linked List
##
## idea: run the linked list with fast and slow to get the midpoint
## and meanwhile reverse the first half!
## then run normally on the second half and reversed firt half!
## A -> E -> C -> B -> A
## fast: ACA; slow: AEC, and reversed CEA for first half to compare CBA
## A -> E -> C -> D -> B -> A
## fast: ACB; slow: AEC, and reversed CEA for first half to compare DBA        
##
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None or head.next == None: return True
        if head.next.next == None:
            if head.val != head.next.val: return False
            return True
            
        fast = head
        slow = head
        prev= None
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next   ## note fast needs to be ahead slow, otherwise fast cannot run
            nextSlow = slow.next
            slow.next = prev
            prev= slow
            slow = nextSlow
            
        ## now slow should be the midpoint
        if fast.next != None:  ## the length of the list is even
            nextSlow = slow.next
            slow.next = prev
            prev= slow
            slow = nextSlow
        else:                  ## the length of the list is odd
            slow = slow.next
        
        while slow.next != None and prev.next != None:
            if slow.val != prev.val: return False
            slow = slow.next
            prev = prev.next
        if slow.val != prev.val: return False
        return True
        
        
        
class Solution2(object):
    ## given the middle node, and first half has been reverse.
    ## then the compare the first half and the second half
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next == None: return True
                
        len_list = self.getLength(head)
        
        if len_list % 2 == 0:
            half_len = len_list // 2
            reverse_head, reverse_next = self.reverseList(head, half_len)
            head1, head2 = reverse_head, reverse_next
        else:
            half_len = len_list // 2 +1
            reverse_head, reverse_next = self.reverseList(head, half_len)
            head1, head2 = reverse_head.next, reverse_next
        
        reverse_head, reverse_next = self.reverseList(head, half_len)
        
        node1, node2 = head1, head2
        while node1 != None and node2 != None:
            if node1.val != node2.val:
                return False
            node1, node2 = node1.next, node2.next
        return True

    def getLength(self, head):
        if not head: return 0
        length = 1
        node = head
        while node.next != None:
            node = node.next
            length += 1
        return length
        
    def reverseList(self, head, half_len):
        if not head: return 
        prev = None
        node = head
        length = 1
        while node.next != None and length < half_len:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
            length += 1
            
        nextNode = node.next
        node.next = prev
        
        return node, nextNode
        