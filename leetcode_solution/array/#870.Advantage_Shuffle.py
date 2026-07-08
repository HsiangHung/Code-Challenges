#
#  870. Advantage Shuffle
#
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        * sort nums1
        * insert ans, by looking slightly larger than nums2[i] from nums1
        * if adv = len(nums1), we should have no None in ans
        * if adv < len(nums1), backfill remaining number in nums1 to ans
        """
        nums1 = sorted(nums1)

        def search(arr, target):
            l, r = 0, len(arr)  # hi is exclusive, search space is [lo, hi)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] <= target:
                    l = mid + 1  # mid can't be the answer, go right
                else:
                    r = mid      # mid could be the answer, keep it in range
            return l if l < len(arr) else None

        
        # backfill numbers reamining in nums1 if None in ans:
        ans = [None] * len(nums1)
        for i in range(len(nums2)):
            larger_idx = search(nums1, nums2[i])
            if larger_idx is not None:
                ans[i] = nums1[larger_idx]
                nums1.pop(larger_idx)
        
        for i in range(len(ans)):
            if ans[i] is None:
                val = nums1.pop(0)
                ans[i] = val

        return ans
