#  493. Reverse Pairs (hard)
#  https://leetcode.com/problems/reverse-pairs/
#
class Solution:
    '''
    https://www.youtube.com/watch?v=j68OXAMlTM4
    https://zhuanlan.zhihu.com/p/111612901
    
    Use merge sort to partition, and during merge, count the pairs between left and right arrays.

    This code is probably correct, but cannot pass through Leetcode test cases. @2020.1.14
    '''
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0   
        self.pairs = 0
        self.mergeSort(nums)
        return self.pairs

    def mergeSort(self, nums):
        if len(nums) <= 1: return nums
        
        mid = len(nums) // 2
        
        left, right = nums[:mid], nums[mid:]        
        left, right = self.mergeSort(left), self.mergeSort(right)
        
        search = True
        j = 0
        while search and j < len(right):  # count nums[i] > 2*nums[j] here 
            i, search = len(left)-1, False
            while i >= 0 and left[i] > 2*right[j]:
                self.pairs += 1
                i -= 1
                search = True
            j += 1

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            
        if i < len(left): nums[k:] = left[i:]
        if j < len(right): nums[k:] = right[j:]
            
        return nums