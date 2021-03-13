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

        insert = False
        if len(intervals) == 0 or newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
            insert = True
        elif newInterval[0] >= intervals[-1][0]:
            intervals.append(newInterval)
            insert = True
        
        i = 0
        while i < len(intervals)-1: # part of this iteration is the similar to 56. merge interval.
            
            if not insert and intervals[i+1][0] > newInterval[0] >= intervals[i][0]: # NOTE >= is important
                intervals.insert(i+1, newInterval)
                insert = True
            
            if intervals[i+1][0] <= intervals[i][1]: # NOTE >= is important
                intervals[i] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)
            else:
                i += 1
                

        return intervals

        