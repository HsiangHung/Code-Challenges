#  252. Meeting Rooms (easy)
#  https://leetcode.com/problems/meeting-rooms/
#
class Solution:
    '''
    O(nlogn) solution
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1][0] < intervals[i][1]:
                return False
            else:
                i += 1
        return True


class Solution2:
    '''
    O(n^2) solution
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if not (intervals[j][0] >= intervals[i][1] or intervals[i][0] >= intervals[j][1]):
                    return False
                    
        return True 