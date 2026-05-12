#  852. Peak Index in a Mountain Array (easy)
#  https://leetcode.com/problems/peak-index-in-a-mountain-array/
#
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) <= 3: 
            max_val = max(arr)
            for i in range(len(arr)):
                if arr[i] == max_val: return i
        
        mid = len(arr) // 2
        
        if arr[mid-1] < arr[mid]  and arr[mid] > arr[mid+1]:
            return mid
        else:
            if arr[mid-1] > arr[mid]:
                return self.peakIndexInMountainArray(arr[:mid])
            elif arr[mid+1] > arr[mid]:
                return mid + 1 + self.peakIndexInMountainArray(arr[mid+1:])
        