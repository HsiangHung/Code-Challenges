#
# 435. Non-overlapping Intervals
#
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        trick sort end time, and pop out the schedule with previous overlaps 
        1. [[1,100],[11,22],[1,11],[2,12]]
           => [[1,11],[2,12],[11,22],[1,100]]
        2. [[1, 11], [11, 22], [23, 50], [1, 100]]
        """

        intervals = sorted(intervals, key=lambda x: x[1])
        m = len(intervals)

        i = 1
        while i < len(intervals)-1:
            a, b = intervals[i]
            if a < intervals[i-1][1]:
                intervals.pop(i)
            else:
                i += 1
        
        if len(intervals) > 1:
            # since previous i loop only up to len(..)-1, here need to check
            if intervals[-1][0] < intervals[-2][1]:
                intervals.pop()
        
        return m - len(intervals)
