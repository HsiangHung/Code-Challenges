# #1460. Make Two Arrays Equal by Reversing Sub-arrays 
# 
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        target_dict = self.get_dict(target)
        arr_dict    = self.get_dict(arr)
        
        return target_dict == arr_dict
        
        
    def get_dict(self, arr):
        arr_dict = {}
        for num in arr:
            arr_dict[num] = arr_dict.get(num, 0) + 1
        return arr_dict