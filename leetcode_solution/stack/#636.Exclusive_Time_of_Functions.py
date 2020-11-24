#  636. Exclusive Time of Functions (medium)
#  https://leetcode.com/problems/exclusive-time-of-functions/
#
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:        
        '''
        https://www.youtube.com/watch?v=k2ZvDK6ze0Q
        https://blog.csdn.net/fuxuemingzhu/article/details/79537000
        
        Trick1: always need to memorize prevTime
        Trick2: if len(stack) > 0 and incoming job type="start", NO pop stack.
                That means later we will have job "end" to close.
        '''
        if n == 1: return [int(logs[-1].split(":")[-1])+1]
              
        exec_time = [0]*n
        
        stack = []
        prevTime = None
        for i in range(len(logs)):
            id, type, time = logs[i].split(":")
            if type == "start":
                if len(stack) > 0:
                    exec_time[stack[-1]] += int(time) - prevTime
                stack.append(int(id))
                prevTime = int(time)
            else:
                exec_time[stack[-1]] += int(time) - prevTime + 1
                stack.pop()            
                prevTime = int(time) + 1
            
        return exec_time

    
    