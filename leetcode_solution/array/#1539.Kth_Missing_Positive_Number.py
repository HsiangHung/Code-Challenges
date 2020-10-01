# 1539. Kth Missing Positive Number
#
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        arr = set(arr)
        
        i = 1
        while i <= 2**31-1 and k > 0:
            if i not in arr:
                k -= 1
            i += 1
            
        return i-1