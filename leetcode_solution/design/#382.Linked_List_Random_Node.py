#  382. Linked List Random Node (medium)
#  https://leetcode.com/problems/linked-list-random-node/
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    https://en.wikipedia.org/wiki/Reservoir_sampling
    https://www.educative.io/edpresso/what-is-reservoir-sampling
    
    Reservoir sampling
    Copy the first k elements from the input array to the output array.
    Iterate from k to n-1 (both inclusive). In each iteration j:
    1. Generate a random number numnum r,  0 <= r <= j. 
    2. If numnum is r < k, replace the element at index numnum in the output array with the item 
       at index j in the input array.
      
    e.g. k=1, n=6, [a,b,c,d,e,f]
         * at j = 0 we have [a]
         * at j = 1, r could be 0, 1. b be selected is 0 <= r < 1, prob = 1/2; 
                                       not selected is r = {1}, p = 1/2
         * at j = 2, r could be 0, 1, 2. c be selected is 0 <= r < 1, prob = 1/3; 
                                          not selected is r = {1,2}, p = 2/3
         
         assume d is selected at j=3, and through all 6 numbers c still in arry, 
                d, e, f should not be selected. p = 1/4 * (1-1/5) * (1-1/6) = 1/6 = 1/n
    '''
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random 
                
        count = 0
        node = self.head
        while node:
            if random.randint(0, count) == 0:
                ans = node.val
            node = node.next
            count += 1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()