
# A. Linked-list

### The linked list nodes are defined as
```Python
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
```

## Q1: Remove Duplicates from Sorted List

```Python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return 
    
        node = head
        while node.next != None:
            nextNode = node.next
            if nextNode.val == node.val:
                if nextNode.next != None:
                    nextNextNode = nextNode.next
                    node.next = nextNextNode
                else:
                    node.next = None
            else:
                node = nextNode
                
        return head
```

## Q2: [Leetcode#21] Merge Two Sorted Lists
### Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
```Python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        if l1 == None: return l2
        if l2 == None: return l1
        
        if l1.val < l2.val:
            head = l1
            node = head
            other = l2
        else:
            head = l2
            node = head
            other = l1
            
        while node.next != None:
            nextNode = node.next
            nextval = nextNode.val
            otherval = other.val
            if nextval <= otherval:
                node = node.next
            else:
                node.next = other
                other = nextNode
                node = node.next
            
        node.next = other
        
        return head
```

## Q3: [Leetcode#24] Swap Nodes in Pairs
### Given a linked list, swap every two adjacent nodes and return its head.
```Python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node == None or node.next == None: return node
        if node.next.next == None:
            nextNode = node.next
            nextNode.next = node
            node.next = None
            return nextNode

        prev= None
        while node.next != None and node.next.next != None:
            nextNode = node.next
            nextNextNode = nextNode.next
            ## -- check head ---
            if head == node: head = nextNode
            ## -- flip--
            if prev != None: prev.next = nextNode
            nextNode.next = node
            node.next =nextNextNode
            prev = node
            ## -- flip is done --
            node = nextNextNode
            
        if node.next != None:
            nextNode = node.next
            prev.next = nextNode
            nextNode.next = node
            node.next = None
        else:
            prev.next = node
            node.next = None
        
        return head
```
