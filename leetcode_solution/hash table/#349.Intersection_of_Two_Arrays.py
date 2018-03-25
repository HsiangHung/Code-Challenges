# [#349]  Intersection of Two Arrays
#
#
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = set(nums1), set(nums2)
        lens1, lens2 = len(nums1), len(nums2)
        if lens1 >= lens2:
            return [num for num in nums2 if num in nums1]
        else:
            return [num for num in nums1 if num in nums2]