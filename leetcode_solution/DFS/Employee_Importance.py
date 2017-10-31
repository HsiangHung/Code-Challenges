# [leetcode#690] Employee Importance
#
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if employees == []: return 0
        
        imp_value = 0
        for employee in employees:
            if employee.id == id:
                imp_value += employee.importance
                for sub_id in employee.subordinates:
                    imp_value += self.getImportance(employees, sub_id)
                
        return imp_value