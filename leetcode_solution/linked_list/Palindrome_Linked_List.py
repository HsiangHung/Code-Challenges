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

class Solution(object):
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