#
#  2095. Delete the Middle Node of a Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        two linked-list run in parallel
        * list-1 moves one node at a time
        * list-2 moves two node at a time
        
        if list-2 to ned, list-1 moves to nearby middle node (depends on even/odd)
        e.g. odd 
        list-1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        list-2: 1 -> 3 -> 5 -> 7 
        after 7, no node. So 4 is middle

        e.g. even
        list-1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
        list-2: 1 -> 3 -> 5 -> 7 
        after 7, no doube node, but 7.next -> 8. So 4->5 middle node

        time complexity O(n), space O(1)
        """

        if not head or not head.next:
            return None

        list1, list2 = head, head
        res = list1 # make sure res == list1, not == head. 
        prev = None
        while list2.next and list2.next.next:
            prev = list1
            list1 = list1.next
            list2 = list2.next.next

        if list2.next:
            middle = list1.next
            prev = list1
        else:
            middle = list1
        middle_next = middle.next
        prev.next = middle_next
        return res
