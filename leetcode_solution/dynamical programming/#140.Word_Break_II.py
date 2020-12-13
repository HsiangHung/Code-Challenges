#  140. Word Break II (hard)
#  https://leetcode.com/problems/word-break-ii/
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        in addition to the dp = {True, False}, need to store the next pointer.
        e.g. s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
        
        we got dp = [True, False, False, True, True, False, False, True, False, False, True]
               next_pointer = {0: [3, 4], 3: [7], 4: [7], 7: [10]}
        meaning, 0->3 or 0->4, then 0->3->7 or 0->4->7, then 0->3->7->10 or 0->4->7->10
        This step is carried out using DFS
        
        Note if dp[-1] = False, return empty list
        '''
        char_dict = {}
        
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        next_pointer = {}
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dp[i]:  # note, here we update only if dp[i]=True
                    dp[j] = True
                    next_pointer[i] = next_pointer.get(i, []) + [j]
                
        print (dp)
        print (next_pointer)
        if not dp[len(s)]:
            return []
        else:
            self.ans = []
            self.DFS(s, 0, [], next_pointer)
            return [" ".join(x) for x in self.ans]
            
            
    def DFS(self, s, i, path, next_pointer):
        if i == len(s):
            self.ans.append(path)
            return
        
        if i not in next_pointer: return  # trick 2, behind append path to self.ans
        
        for x in next_pointer[i]:
            self.DFS(s, x, path + [s[i:x]], next_pointer)
        
