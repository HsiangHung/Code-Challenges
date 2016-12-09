## Q 2.7 Check if a linked list is a palindrome.
#
# idea: create a reversed linked list, and then go through this and the reverse
#

def isPalindrome(h1,h2):
	node = h1
	rnode = h2
	while node != None and rnode != None:
		if node.val != rnode.val: return False
		node = node.next
		rnode = rnode.next
		
	return True

## this function is used to reverse the linked list
def reverse_list(head):
    node = head
    prev = None
    while node.next != None:
        print (node.val)
        nextNode = node.next
        node.next = prev
        prev = node
        node = nextNode
    node.next = prev
    return node

head = reverse_list(A)
print isPalindrome(A, head)