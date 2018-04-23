## [#582] Kill Process
#
#  Bloomberg
#
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        parent_dict = {}
        for i in range(len(pid)):
            if ppid[i] not in parent_dict:
                parent_dict[ppid[i]] = [pid[i]]
            else:
                parent_dict[ppid[i]].append(pid[i])
            
        return self.killing(parent_dict, kill)
    
    def killing(self, parent_dict, kill):
        if kill not in parent_dict:
            return [kill]
        
        killed_pid = [kill]
        for child in parent_dict[kill]:
            killed_pid += self.killing(parent_dict, child)
        
        return killed_pid
