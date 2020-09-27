# # 977. Squares of a Sorted Array
#
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        first find minimum squared value and then zig-zag search.
        '''
        
        min_square, idx = A[0]**2, 0
        for i in range(1, len(A)):
            if A[i]**2 < min_square:
                min_square = A[i]**2
                idx = i
                
        output = []
        while len(A) > 0:                        
            if 0 < idx < len(A) - 1:
                A1, A2 = A[idx-1], A[idx+1]
                if abs(A1) <= abs(A2): 
                    new_idx = idx - 1
                else:
                    new_idx = idx
            elif idx == 0:
                new_idx = idx
            elif idx == len(A) - 1:
                new_idx = idx - 1
            
            output.append(A[idx]**2)
            A.pop(idx)
            
            idx = new_idx
                
        return output