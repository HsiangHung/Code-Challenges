#  57. Insert Interval (medium)
#  https://leetcode.com/problems/insert-interval/
#
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        two part:
        1. since intervals is a sorted list, find the right position to insert newInterval
        2. then the procedure is the same as 56. merge intervals.
        '''
        if len(intervals) == 0:
            return [newInterval]
        else:
            if newInterval[1] < intervals[0][0]: 
                return [newInterval] + intervals
            elif newInterval[0] > intervals[-1][1]:
                return intervals + [newInterval]
        
        # find the right position to insert "newInterval"
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            i += 1
            
        intervals.insert(i, newInterval)

        # thr following is the same process as 56. merge interval.
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1][0] > intervals[i][1]:
                i += 1
            elif intervals[i+1][0] <= intervals[i][1]:
                intervals[i][0] = min(intervals[i+1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
                intervals.pop(i+1)
                
        return intervals
                
                
            