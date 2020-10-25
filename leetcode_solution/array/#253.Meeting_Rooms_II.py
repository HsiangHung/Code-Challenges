# #253. Meeting Rooms II
#
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        http://cqbbshuashua.blogspot.com/2018/04/253-meeting-rooms-ii.html
        
        * prepare intervals =  [(s1,e1), (s2,e2), (s3,e3),...] as
          start = [(s1, 0), (s2, 1), (s3, 2), .....]
          end = [(e1, 0), (e2, 1), (e3, 2), .....]
        * sort start and end by time for each:
          start = [(s3, 2), (s2, 1), (s1, 0), .....]
          end = [(e2, 1), (e3, 2), (e0, 0), .....]
        * initialize rooms set and loop through the start list,  
          i.e. rooms = [2]
               if s2 < e1: rooms = [2, 1] 
               if s1 > e2: rooms = [2]
               if s1 > e3: rooms = []
               
           so the number rooms needs is 2.          
        '''
        if intervals == []: return 0

        start = [(intervals[i][0], i) for i in range(len(intervals))]
        end = [(intervals[i][1], i) for i in range(len(intervals))]
                
        start = sorted(start, key = lambda x: x[0])  # sort start list by time
        end = sorted(end, key = lambda x: x[0])      # sort end list by time
        
        rooms = set({})
        
        i, j = 1, 0
        rooms = set({start[0][1]})
        max_rooms = 1
        while i <= len(start)-1 and j <= len(end)-1:
            if start[i][0] < end[j][0]:
                rooms.add(start[i][1])
                max_rooms = max(max_rooms, len(rooms))
                i += 1
            else:
                rooms.remove(end[j][1])
                j += 1
        
        return max_rooms
            
        
        