# 109. Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        solution version to use linked-list
        tricl-1: using self.get_half to get middle node: fast moves x2 and slow moves x1
        trick-2: if mid_node = head, stop recursion
        trick-3: everytime when getting mid_node, remove node before mid_node, otherwise
                 cannot stop linked-list.
        '''
        
        return self.build_BST(head)
        
        
    def build_BST(self, head):
        if not head: return None
        
        mid_node = self.get_half(head)
        root = TreeNode(val=mid_node.val)
        
        if mid_node == head: return root  # trick-2
        
        root.left = self.build_BST(head)
        root.right = self.build_BST(mid_node.next)
        
        return root
    
    
    def get_half(self, head):
        '''
        trick-1 to get middle node
        '''
        if not head or not head.next: return head
        
        fast, slow = head, head
        prev = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev= slow
            slow = slow.next
        
        prev.next = None   # trick-3, remove node before mid_node
        return slow
        