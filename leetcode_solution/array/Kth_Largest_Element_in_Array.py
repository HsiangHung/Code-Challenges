## [Leetcode#215] Kth Largest Element in an Array
##
##  idea: prepare a k-dimension array, and always make numbers in the array in order
##
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarray = [nums[0]]
        for i in range(1, len(nums)):
            #print nums[i], subarray
            if nums[i] >= subarray[len(subarray)-1]:
                subarray.append(nums[i])
                if len(subarray) > k: subarray.remove(subarray[0])
            elif nums[i] < subarray[0]:
                if len(subarray) < k: subarray.insert(0, nums[i])
            else:
                for m in range(len(subarray)-1):
                    if subarray[m] <= nums[i] <= subarray[m+1]:
                        subarray.insert(m+1, nums[i])
                        if len(subarray) > k: subarray.remove(subarray[0])
                        break

        return subarray[0]   