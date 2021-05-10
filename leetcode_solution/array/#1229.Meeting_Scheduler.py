#  1229. Meeting Scheduler (medium)
#  https://leetcode.com/problems/meeting-scheduler/
#
class Solution:
    '''
    https://www.cnblogs.com/seyjs/p/11713518.html
    
    make sure sort slots1 and slot2 first.
    '''
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if len(slots1) == 0 or len(slots2) == 0: return []
                
        slots1 = sorted(slots1, key = lambda x: x[0])
        slots2 = sorted(slots2, key = lambda x: x[0])
        
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            
            if slots2[j][1] < slots1[i][0]:
                j += 1
            elif slots1[i][1] < slots2[j][0]:
                i += 1
            else:
                start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
                if end - start >= duration:
                    return [start, start + duration]
                    
                if slots1[i][1] < slots2[j][1]:
                    i += 1
                else:
                    j += 1
        
        return []
        