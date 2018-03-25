# [#142] Linked List Cycle II
#
#  e.g. if 1->2->3->4->5->6->2.... begin at 2
#
#   slow: 1->2->3->4->5->6  (each move one node)
#   fast: 1->3->5->2->4->6  (each move two node)
#
#    meet at 6, then the fast node "6" is replaced by head, and the fast list
#    tunes back to each move one node
#
#    slow: 5->6->2->3...
#    fast: 4->1->2
#     
#    now meet at 2, so 2 is the answer.
#
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: return None
        
        slow, fast = head, head
        isCycle = False
        while slow.next != None and fast.next != None and fast.next.next != None and not isCycle:
            nextSlow = slow.next
            nextFast = fast.next.next
            if nextSlow == nextFast:
                isCycle = True
            else:
                slow = nextSlow
                fast = nextFast
            
        if not isCycle: return None
    
        slow, fast = nextSlow, head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow