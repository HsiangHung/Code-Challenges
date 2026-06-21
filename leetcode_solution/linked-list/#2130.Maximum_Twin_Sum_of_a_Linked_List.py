#
# 2130. Maximum Twin Sum of a Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head.next:
            return head.val

        def get_reverse_linked(head):
            """
            This creates a new linked list,reverse to head
            not going to change the original linked list
            """
            if not head and not head.next:
                return head
            prev, node = None, ListNode(val=head.val)
            curr = head # not change
            while curr and curr.next:
                next_node = ListNode(val=curr.next.val)
                node.next = prev
                prev = node
                node = next_node
                curr = curr.next
            node.next = prev
            return node

        reverse_head = get_reverse_linked(head)

        max_twin_sum = -float("inf")
        node, r_node = head, reverse_head
        while node:
            print(node.val, r_node.val)
            max_twin_sum = max(max_twin_sum, node.val + r_node.val)
            node = node.next
            r_node = r_node.next
        
        return max_twin_sum
