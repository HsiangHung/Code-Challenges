#  57. Insert Interval (medium)
#  https://leetcode.com/problems/insert-interval/
#
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        The procedure is the same as 56. merge intervals, but first insert newInterval before merge 
        if necessary
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
#
#
#
class Solution2:
    '''
    two part: (1) binary search to insert newInterval and (2) then merge as #56
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = self.search(intervals, newInterval)
        intervals.insert(index, newInterval)
        
        i = 0
        while i < len(intervals)-1:
            a, b = intervals[i], intervals[i+1]
            if b[0] <= a[1]:
                intervals[i] = [min(a[0], b[0]), max(a[1], b[1])]
                intervals.pop(i+1)
            else:
                i += 1
                
        return intervals
        
        
    def search(self, intervals, newInterval):
        if len(intervals) == 0: return 0
        if len(intervals) == 1:
            return 1 if newInterval[0] > intervals[0][0] else 0
                            
        mid = len(intervals) // 2
            
        if intervals[mid][0] > newInterval[0] >= intervals[mid-1][0]:
            return mid
        elif newInterval[0] > intervals[mid][0]:
            return mid + self.search(intervals[mid:], newInterval)
        else:
            return self.search(intervals[:mid], newInterval)
    



        