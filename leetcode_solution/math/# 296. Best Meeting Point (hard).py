#  296. Best Meeting Point (hard)
#  https://leetcode.com/problems/best-meeting-point/
#
class Solution:
    '''
    shortest distance is given by midean value of x and y lists.
    '''
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        x, y = [], []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    x.append(i)
                    y.append(j)
        
        x2, y2 = x[:], y[:]
       
        k = len(x) // 2
        if len(x) % 2 == 1:
            m_x, m_y = self.quick_select(x, 0, len(x)-1, k+1), self.quick_select(y, 0, len(y)-1, k+1)
        else:
            self.quick_sort(x, 0, len(x)-1), self.quick_sort(y, 0, len(y)-1)
            m_x, m_y = 0.5*(x[k] + x[k-1]), 0.5*(y[k] + y[k-1])
            
        return int(sum([abs(x2[i]-m_x)+abs(y2[i]-m_y) for i in range(len(x2))]))
    
    
    def quick_select(self, arr, first, last, k):
        if last - first + 1 >= k > 0:
            split = self.partition(arr, first, last)
            
            if k == split - first + 1:
                return arr[split]
            elif k > split - first + 1:
                return self.quick_select(arr, split+1, last, k - (split - first + 1))
            else:
                return self.quick_select(arr, first, split-1, k)
    
    
    def quick_sort(self, arr, first, last):
        if first < last:
            split = self.partition(arr, first, last)
            self.quick_sort(arr, first, split-1)
            self.quick_sort(arr, split+1, last)
            
    def partition(self, arr, first, last):
        pivot = arr[first]
        L, R = first + 1, last
        
        done = False
        while not done:
            while L <= R and arr[L] <= pivot:
                L += 1

            while L <= R and arr[R] >= pivot:
                R -= 1
                
            if L > R:
                done = True
            else:
                arr[L], arr[R] = arr[R], arr[L]
                
        arr[first], arr[R] = arr[R], arr[first]
        return R            
   