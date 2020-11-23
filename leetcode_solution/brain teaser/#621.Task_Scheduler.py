#  621. Task Scheduler (medium)
#  https://leetcode.com/problems/task-scheduler/
#
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        http://bookshadow.com/weblog/2017/06/18/leetcode-task-scheduler/
        https://www.cnblogs.com/grandyang/p/7098764.html
        
        e.g.
        1. tasks = ["A","A","A","B","B","B"], n = 2
            "A" and "B" appear 3 times
            Aoo Aoo A => ABo ABo AB => insert idle => ABi ABi AB
            return (n+1)*(3-1) + 2 = 8
            
        2. tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
           "A" appears 6 times
             Aoo Aoo Aoo Aoo Aoo Aoo => ABo Aoo Aoo Aoo Aoo Aoo
          => ABC Aoo Aoo Aoo Aoo Aoo => ABC ADo Aoo Aoo Aoo Aoo
          => ABC ADE Aoo Aoo Aoo Aoo => ABC ADE AFG Aoo Aoo Aoo
          => ABC ADE AFG Aii Aii A => return (n+1)*(6-1) + 1 = 16
          
        3. tasks = ["A","A","A","A","A","B","B","B","B","B",
                    "C","C","C","C","D","D","E"], n = 5
             "A" appears 5 times
             Aooooo Aooooo Aooooo Aooooo A => ABoooo ABoooo ABoooo ABoooo AB
          => ABCDEo ABCDoo ABCooo ABCooo AB => ABCDEi ABCDii ABCiii ABCiii AB
          => return (n+1)*(5-1) + 2 = 26
    
        4. task = ["A","A","A","B","B","B","C","C","C","D","D","E"], n=2
             "A", "B", "C" appears 3 times
             Aoo Aoo Aoo => ABo ABo ABo => ABC ABC ABC => ABC ABC ABC Doo D
             => ABC ABD ABC DEC
             
             
        Look for most-frequently appeared tasks, and then insert n betweem them
        '''
        
        if n == 0: return len(tasks)
        
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        max_freq = max(freq.values())
        
        num_tasks_max_freq = sum([1 for task in freq if freq[task] == max_freq])
        return max(len(tasks), (n+1)*(max_freq-1) + num_tasks_max_freq)
 