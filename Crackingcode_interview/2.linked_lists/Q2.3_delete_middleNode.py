## 2.3 Remove the middle node only given access to the middle node
#
# e.g. linked list is [3,2,5,9,2,10,9], given 9 to have [3,2,5,2,10,9]
#

def delete_middle_node(middle):
    if middle == None or middle.next == None: return
    nextNode = middle.next
    middle.val = nextNode.val
    middle.next = nextNode.next
    return



delete_middle_node(D)

## test function

node = A
while node.next != None:
    print(node.val)
    node = node.next
print(node.val)