#  729. My Calendar I (medium)
#  https://leetcode.com/problems/my-calendar-i/
#
class MyCalendar:
    '''
    self.events = [(s1,e1), (s2,e2),....] order by start time
    if only (s,e) such that s >= s(i) and e <= s(i+1) we can book.
    use binary search
    '''
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
                
        if len(self.events) == 0:
            self.events.append((start, end))
            return True
        else:
            if start >= self.events[-1][1]:
                self.events.append((start, end))
                return True
            elif end <= self.events[0][0]:
                self.events.insert(0, (start, end))
                return True
            
            idx = self.search(start, self.events)
                    
            if start >= self.events[idx][1] and end <= self.events[idx+1][0]:
                self.events.insert(idx+1, (start, end))
                return True
            else:
                return False
        
        
    def search(self, start, events):
        if len(events) == 1:
            return 0 if start > events[0][0] else -1
        
        if len(events) == 2:
            return 1 if start > events[1][0] else 0
        
        mid = len(events) // 2
        
        if events[mid][0] <= start < events[mid+1][0]:
            return mid 
        elif start > events[mid+1][0]:
            return self.search(start, events[mid+1:]) + mid + 1
        else:
            return self.search(start, events[:mid+1]) 
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)