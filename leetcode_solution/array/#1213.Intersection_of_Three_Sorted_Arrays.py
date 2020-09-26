# #1213. Intersection of Three Sorted Arrays
#
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        intersect = set({})
        
        arr3 = set(arr3)
        for x in arr2:
            if x in arr3:
                intersect.add(x)
            
        arr1 = set(arr1)
        for x in intersect.copy():
            if x not in arr1:
                intersect.remove(x)
                
                
        return sorted(list(intersect))