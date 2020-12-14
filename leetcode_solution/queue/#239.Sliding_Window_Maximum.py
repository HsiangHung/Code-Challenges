#  239. Sliding Window Maximum (hard)
#  https://leetcode.com/problems/sliding-window-maximum/
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        https://www.youtube.com/watch?v=ShbRCjvB_yQ
        
        prepare a queue, and make sure in the queue, index in ascending order and num in descrending order
        then sliding window. if first element index is out of window, pop out.
        the new incoming is inserted into queue until its val < elements in queue.
        
        e.g. nums = [1,3,-1,-3,5,3,6,7] k = 3, q = []
                     0 1  2  3 4 5 6 7
        
        1. i=0 [(0,1)]
        2. i=1 [(1,3)] since 3 >= 1, pop out (0,1)
        3. i=2 [(1,3), (2,-1)], insert in -1 since -1 < 3
        4. i=3 [(1,3), (2,-1), (3,-3)], insert in since -3 < -1
        5. i=4 [(2,-1),(3,-3)] since (1,3) out of window, but incoming 5>-3 and 5>-1
               => q = [(4,5)]
        6. i=5 [(4,5), (5,3)]
        7. i=6 [(6,6)] since 6 >= 3 and 6 >= 5. So both pop out
        8. i=7 [(7,7)] since 7 >= 6 So 6 pop out
        
        in this case we have first element always largest val and the index within the window
        '''
        queue = []
        ans = []
        for i in range(len(nums)):
            
            while len(queue) > 0 and nums[i] > queue[-1][1]:
                queue.pop(-1)
            queue.append((i, nums[i]))
            
            if queue[0][0] <= i-k: queue.pop(0)
            
            if i >= k-1:
                ans.append(queue[0][1])
            
        return ans
