#  282. Expression Add Operators (hard)
#  https://leetcode.com/problems/expression-add-operators/
#
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        '''
        https://wdxtub.com/interview/14520604912510.html
        http://bookshadow.com/weblog/2015/09/16/leetcode-expression-add-operators/
        
        e.g. num = "1234", need to go 
        ["1","234"], ["1","2","34"],["1","2","3","4"]
        ["12","34"], ["12","3","4"] ....
        and insert opertation "+", "-", "*" between any two numbers
        
        NOTE: for "+", "-" DFS is straightforward. But for "*", we need to keep track last number which
        has "+"/"-", and do muplitcation operation on the number. i.e. 
        
        ["1","+","2"], result = 1+2=3
        if comes "*","3", we need to update as => ["1","+","2*3"] = ["1","+","6"]
        
        Three to store, expression, stack for real operation (keep track last number) and real result.
        e.g. ex = "1+2*3",   stack = ["1","+","6"],  result =  7
             ex = "1+2*3*4", stack = ["1","+","24"], result = 25
        '''
        self.ans = []
        if num == "": return self.ans       
        
        for i in range(len(num)):
            if len(num[:i+1]) > 1 and num[0] == "0": continue
            self.DFS(num[i+1:], target, num[:i+1], [int(num[:i+1])], int(num[:i+1]))
        return self.ans
                
                
    def DFS(self, num, target, ex, stack, result):
        
        if num == "":
            if result == target: 
                self.ans.append(ex)
            return
        
        for i in range(len(num)):
                        
            if len(num[:i+1]) > 1 and num[0] == "0": continue   ## trick: for example "02", then we skip
            
            y = num[:i+1]

            self.DFS(num[i+1:], target, ex+"+"+y, stack+["+", int(y)], result+int(y))
            self.DFS(num[i+1:], target, ex+"-"+y, stack+["-", int(y)], result-int(y))
                        
            stack2 = stack[:]    # NOTE here we need to assign another stack2, if directly use stack
                                 # in "*" DFS, it will impact values for other recursion processes.
            if len(stack2) >=2:  # case of stack = ["1","+","2"]
                op, x = stack2[-2], int(stack2[-1])
                stack2[-1] = x*int(y)
                if op == "+":
                    self.DFS(num[i+1:], target, ex+"*"+y, stack2, result-x+x*int(y))
                elif op == "-":
                    self.DFS(num[i+1:], target, ex+"*"+y, stack2, result+x-x*int(y))
            else:                # case of stack = ["1"], no operation needs to worry
                x = int(stack2[-1])
                stack2[-1] = x*int(y)
                self.DFS(num[i+1:], target, ex+"*"+y, stack2, result-x+x*int(y))
