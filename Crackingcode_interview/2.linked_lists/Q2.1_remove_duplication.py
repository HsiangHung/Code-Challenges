## Q2.1: remove unsorted duplicated linked-list
#
# (a) using additional space O(n) with time O(n)  
# (b) brute force for space O(1) but time O(n^2)
#
# (a) -----------------------------------------------
def remove_dupNode_a(head):
    nodes_set = set({})
    node = head
    prev= None
    while node.next != None:
        if node.val not in nodes_set:
            nodes_set.add(node.val)
            prev = node
            node = node.next
        else:
            nextNode = node.next
            prev.next = nextNode
            node = nextNode
    if node.val in nodes_set: prev.next = None
        
    return head


# (b) -----------------------------------------------
def remove_dupNode_b(head):
    nodeA = head
    while nodeA != None:
        
        #print (nodeA.val)
        
        nodeB = nodeA.next
        prev = nodeA
        
        while nodeB != None:
            if nodeB.val == nodeA.val:
                nodeBNext = nodeB.next
                prev.next = nodeBNext
                nodeB = nodeBNext
            else:
                prev= nodeB
                nodeB = nodeB.next
        if nodeB.val == nodeA.val: prev.next = None        
            
        nodeA = nodeA.next
    
    

    
new_head = remove_dupNode_b(A)

## print test function: -----
printList(new_head)