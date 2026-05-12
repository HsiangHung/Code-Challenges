#  148. Sort List (medium)
#  https://leetcode.com/problems/sort-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Using merge sort
    '''
    def sortList(self, head: ListNode) -> ListNode:
     
        if not head or not head.next: return head
        
        half = self.get_half(head)
        nextHalf = half.next 
        half.next = None      # this is important, without cutting, unlimited recursion
        
        left, right = self.sortList(head), self.sortList(nextHalf)
        
        # first part, separate to two lists
        # ------------------------------------------
        # then merge the two lists
        
        if left.val <= right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        
        node = head
        while left and right:
            if left.val <= right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
    
        node.next = left if not right else right  ## if left or right still not to the end
        
        return head
    
    
    def get_half(self, head):
        if not head: return 
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        