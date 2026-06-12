#
#  933. Number of Recent Calls
#
class RecentCounter:

    def __init__(self):
        self.requests = []
        
    def ping(self, t: int) -> int:
        self.requests.append(t)

        # every time new request in, need to check and remove early request
        i = len(self.requests) - 1
        while i >= 0 and t - self.requests[i] <= 3000:
            i -= 1
        self.requests = self.requests[i+1:]

        return len(self.requests)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)