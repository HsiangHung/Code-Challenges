# #986. Interval List Intersections
#
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        intersect = []
        
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][1]:
                if A[i][1] > B[j][0]:
                    intersect.append([max(A[i][0], B[j][0]), A[i][1]])
                elif A[i][1] == B[j][0]:
                    intersect.append([A[i][1], A[i][1]])
                i += 1
            else:
                if A[i][0] < B[j][1]:
                    intersect.append([max(A[i][0], B[j][0]), B[j][1]])
                elif A[i][0] == B[j][1]:
                    intersect.append([A[i][0], A[i][0]])
                j += 1
        
        
        return intersect