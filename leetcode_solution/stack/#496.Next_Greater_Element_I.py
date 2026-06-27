#
# 496. Next Greater Element I
#
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        stack solution: https://www.youtube.com/watch?v=sDKpIO2HGq0
        But here I simply use dict to solve
        """
        nums2_idx = {}
        for i in range(len(nums2)):
            nums2_idx[nums2[i]] = nums2_idx.get(nums2[i], []) + [i]

        res = []
        for i in range(len(nums1)):
            idx = nums2_idx[nums1[i]][0] + 1
            while idx < len(nums2) and nums2[idx] <= nums1[i]:
                idx += 1

            if idx == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[idx])
        
        return res
