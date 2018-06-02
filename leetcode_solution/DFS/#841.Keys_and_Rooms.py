## [Leetcode#841] Keys and Rooms
#
# Google
#
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        num_rooms = len(rooms)
        self.roomVisited = set({})
        
        self.visiting(0, rooms)
                        
        return len(self.roomVisited) == num_rooms
    
    
    def visiting(self, key, rooms):
        if key in self.roomVisited: return
        self.roomVisited.add(key)
        
        if len(self.roomVisited) == len(rooms): return
 
        if len(rooms[key]) > 0:
            for room_key in rooms[key]:
                self.visiting(room_key, rooms)