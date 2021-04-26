#  332. Reconstruct Itinerary (medium)
#  https://leetcode.com/problems/reconstruct-itinerary/
#
class Solution:
    '''
    https://www.youtube.com/watch?v=WYqsg5dziaQ 
    
    using dict[depart] = [arrival1, arrival2, ...] as data structure
    
    if ticket (depart, arrrival2) is used, update dict[depart][2] = 0 to next step,
    if doesn't work, backtrack to dict[depart][2] = arrival2
    
    '''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        trip_dict = {}
        for trip in tickets:
            trip_dict[trip[0]] = trip_dict.get(trip[0], []) + [trip[1]]
            
        for city in trip_dict:
            trip_dict[city] = sorted(trip_dict[city])
        
        self.ans = None
        self.DFS(trip_dict, ["JFK"], len(tickets)+1)
        return self.ans
    
        
    def DFS(self, trip_dict, itinerary, target):
        if len(itinerary) == target:
            self.ans = itinerary
            return
        
        city = itinerary[-1]
        if city not in trip_dict or self.ans: return
        
        for i in range(len(trip_dict[city])):
            if trip_dict[city][i] != 0:
                arrival = trip_dict[city][i]
                trip_dict[city][i] = 0
                self.DFS(trip_dict, itinerary + [arrival], target)
                trip_dict[city][i] = arrival
  