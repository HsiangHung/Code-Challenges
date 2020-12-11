#  528. Random Pick with Weight (medium)
#  https://leetcode.com/problems/random-pick-with-weight/
#
class Solution:
    '''
    https://www.youtube.com/watch?v=fWS0TCcr-lE
    
    identify buckets. e.g. w = [1,3,2]
    bukets are [[0], [1,2,3], [4,5]]
    
    given r = random.randint(0, 5), the probability ~ the bucket size
    each bucket range starts from previous accumulated sum.
    r = {0} to return 0; r = {1,2,3} to return 1; r = {4,5} to return 2
    Then binary search which bucket it belongs to.
    '''    
    def __init__(self, w: List[int]):
        self.bucket = []
        j = 0
        for i in range(len(w)):
            weight = w[i]
            self.bucket.append([j, j+w[i]-1])
            j += w[i]
        
        self.n = j

    def pickIndex(self) -> int:
        import random
        r = random.randint(0, self.n-1)
        bucket = self.bucket[:]
        return self.search(r, bucket)
    
    def search(self, r, bucket):
        if len(bucket) == 1: return 0
        
        mid = len(bucket) // 2
        
        if bucket[mid][0] <= r <= bucket[mid][1]:
            return mid
        elif r > bucket[mid][1]:
            return mid + 1+ self.search(r, bucket[mid+1:])
        else:
            return self.search(r, bucket[:mid])
