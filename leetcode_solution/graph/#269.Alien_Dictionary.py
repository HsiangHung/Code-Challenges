#  269. Alien Dictionary (hard)
#  https://leetcode.com/problems/alien-dictionary/
#
#  FB high-frequency 
#
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Directed acyclic grapg (DAG) implementation on this problem
        https://www.youtube.com/watch?v=0Gr6g17WozM
        https://www.youtube.com/watch?v=hCrbYOlQFrY 
        Use course and course II manner to perform topological sort.
        
        corner cases:
        1. ["z", "z"] => "z"
        2. ["zy", "zx"] => "yxz", or "zyx" or "yzx", "z" can be any place
        3. ["ab", "abc"] => "abc", or "bca", any order
        4. ["abc", "ab"] => ""
        5. ["wrt","wrtkj"] => "jkrtw", or "twjkr", any order
        6. ["wrtkj","wrt"] => ""
        7. ["ac","ab","b"] => "acb" or "cab"
        8. ["b","ac","ab"] => "cba"
        9. ["wnlb"] => "wnlb"
        '''    
        
        if len(words) == 1: return words[0]
        
        orders, letter_set = {}, set(list(words[0]))
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            l1, l2 = self.compare(w1, w2)
            # print (l1, l2)
            if l2:
                orders[l1] = orders.get(l1, []) + [l2]  # normal case, e.g.["wrt", "wrf"]
            else:
                if l1:
                    orders[l1] = orders.get(l1, []) + [] # e.g. ["ab", "abc"]

            for letter in w2:
                letter_set.add(letter)
            
        # print (orders, letter_set)
                
        self.acyclic = False
        self.sort = []
        visited = {letter: 0 for letter in letter_set} # inital all 0, unvisited
        
        # print (visited)
        
        # --- topological sort ---
        for letter in letter_set:
            self.DFS(letter, orders, visited)
        
        # print (self.acyclic, self.sort)           
        
        return "".join(self.sort[::-1]) if not self.acyclic and len(orders) > 0 else ""        
        
    
    def DFS(self, letter, orders, visited):         
        if visited[letter] != 0:
            if visited[letter] == 1: self.acyclic = True
            return
        
        visited[letter] = 1
        if letter in orders:
            for x in orders[letter]:
                self.DFS(x, orders, visited)
        
        visited[letter] = 2
        self.sort.append(letter)
        
        
    def compare(self, w1, w2):
        i = 0
        while i < min(len(w1), len(w2)) and w1[i] == w2[i]:
            i += 1
        if i == len(w1):      # if like ["ab", "abc"], then order is any comm of "abc"
            return w1, None  
        elif i == len(w2):    # if like ["abc", "ab"], then there is no order
            return None, None
        return w1[i], w2[i]
