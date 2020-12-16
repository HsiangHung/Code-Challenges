#  1574. Shortest Subarray to be Removed to Make Array Sorted (medium)
#  https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
#
class Solution:
    '''
    Running index from head -> and tail <- to get "left" and "right" are sorted arrays
    
    e.g. 
    * [1,2,2,2,1,1,1]: left=[1,2,2,2], right=[1,1,1]
    * [5,4,3,2,1]: left=[5], right=[1]
    * [1,2,3,10,0,7,8,9]: left=[1,2,3,10], right=[0,7,8,9]
    
    to merge, we need to DFS graudually remove left[-1] or right[0] until left[-1] <= right[0]
    '''
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
                
        # first run from 0 until arr[i-1] > arr[i]         
        i = 1
        while i <= len(arr)-1 and arr[i] >= arr[i-1]:
            i += 1        
        
        if i == len(arr):  # e.g. [1,2,3,4] montonic increasing array
            return 0
        elif i < len(arr):
            j = len(arr)-1   # reverse run j from -1, -2, -3... until arr[j-1] > arr[j]
            while arr[j] >= arr[j-1]:
                j -= 1
            
        left, right = arr[:i], arr[j:]  # now, we gaurantee left and right are sorted arrays
        merge = self.DFS(left, right) 
        return len(arr) - len(merge)
        
    def DFS(self, left, right):
        if len(left) == 0: return right
        if len(right) == 0: return left
        if left[-1] <= right[0]: return left + right
        
        a, b = self.DFS(left, right[1:]), self.DFS(left[:-1], right)
        
        if len(a) >= len(b):
            return a
        else:
            return b
     