## Q2.6: find beginning of a circular linked list
#
#  e.g. 0->1->2->3->4->5->6->7->3->4 (circule begins at 3)
#    
#    look up the first meet:
#    slow: 0,1,2,3,4,5
#    fast: 0,2,4,5,3,5
#
#    then move slow to head, and look up second meet:
#    slow: 0,1,2,3,4,5,0,1,2,3
#    fast: 0,2,4,5,3,5,5,6,7,3
#
def getLoop_beginning(head):
    """
    :type node: Linked list
    :rtype: node
    """
    slow_node = head
    fast_node = head
    #print (fast_node.val, slow_node.val)
    while slow_node.next != None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
        if fast_node.val == slow_node.val: break
        print (fast_node.val, slow_node.val)
    print (fast_node.val, slow_node.val)
    
    slow_node = head
    while slow_node.val != fast_node.val:
        slow_node = slow_node.next
        fast_node = fast_node.next
    
    return slow_node.val


# -------------------------
# test function:
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

old_node = Node(0)
head = old_node
for i in range(1,8):
    node = Node(i)
    if i == 3: start = node
    node.prev = old_node
    old_node.next = node
    old_node = node

## making circular linked list:
node.next = start

## check:
node = head
i =0
while i < 20:
    print(i,node.val)
    node = node.next
    i += 1
        
print(getLoop_beginning(head))