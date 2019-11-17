## [#88] Merge Sorted Array
#
#  FB
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
                
        idx, end_idx = 0, m
        
        while len(nums2)>0 and nums2[0] < nums1[end_idx-1] and end_idx < len(nums1):
            if nums1[idx] >= nums2[0]:
                nums1[idx+1:end_idx+1] = nums1[idx:end_idx]
                nums1[idx] = nums2[0]
                idx += 1
                end_idx += 1
                nums2.pop(0)
            elif nums1[idx] < nums2[0]:
                idx += 1
        
        if len(nums2) > 0 and nums2[0] >= nums1[end_idx-1]:
            nums1[end_idx:] = nums2[:]
            
        return nums1