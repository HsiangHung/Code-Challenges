# # 896. Monotonic Array
#
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        if len(A) <= 1: return True
        
        monotonic = set({})
        for i in range(1, len(A)):
            if A[i] - A[i-1] > 0:
                monotonic.add(1)
            elif A[i] - A[i-1] < 0:
                monotonic.add(-1)
    
            if len(monotonic) > 1: return False
            
        
        return True
