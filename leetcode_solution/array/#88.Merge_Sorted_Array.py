#  88. Merge Sorted Array (easy)
#  https://leetcode.com/problems/merge-sorted-array/
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        if nums1[m-1] <= nums2[0]: nums1[m:] = nums2[:]
        
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                nums1.pop()
                m += 1

        if j < n:
            nums1[i:] = nums2[j:]