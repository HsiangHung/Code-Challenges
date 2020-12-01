#  426. Convert Binary Search Tree to Sorted Doubly Linked List (medium)
#  https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# 
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        Use stack, as same manner in BST iterstor problem. 
        Initally go lef, to get stack 
        As long as node has right child, push its go_left(right)
        
        e.g. tree = [4,2,5,1,3]
              action    node  next    stack
        0.                            [4,2,1]
        1.    pop        1            [4,2]
        2.    pop        1       2    [4]
        3.    pointer    1  <=>  2    [4]
        4.               2            [4]
        5.    traverse   2            [4,3]
        6.    pop        2       3    [4]
        7.    pointer    2  <=>  3    [4]
        8.               3            [4]
        9.    pop        3       4    []
        10.   pointer    3  <=>  4    []
        11.              4            []
        12.   traverse   4            [5]
        13.   pop        4       5    []
        14.   pointer    4  <=>  5    []
        15.              5            []
        
        rember the last node need to right connected to head, and head left to the last node
        '''
        if not root: return
        
        self.stack = []
        self.go_left(root)
            
        head = self.stack.pop()

        node = head
        i = 0
        while self.stack or node.right:
                    
            if node.right: 
                self.go_left(node.right)
                                
            nextNode = self.stack.pop()
            
            node.right = nextNode
            nextNode.left = node
            node = nextNode
        
        node.right = head
        head.left = node
                
        return head
        
    def go_left(self, node):
        self.stack.append(node)
        while node.left:
            node = node.left
            self.stack.append(node)
        
        
