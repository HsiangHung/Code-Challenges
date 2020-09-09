# #721. Accounts Merge
#
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        * https://codeleading.com/article/60652794759/
        * https://www.jianshu.com/p/15a23f2833ca
        * https://blog.csdn.net/fuxuemingzhu/article/details/82913712
        
        Although this problem is rated as medium, it is quite complicated.
        Two steps:
        (1) build name-mail dictionary as {name: [[email1, email2], [email2, email5]]}
            loop through new_account = [mail4, email1] from "accounts", and check
            if emails in dict, e.g. [email1, email2], [email2, email5] have union email 
            to new_account. If yes, [email1, email2] union as [email1, email2, email4].
        (2) Note now there may exist need-union email accounts in dict:
            {name: [[email1, email2, email4], [email2, email5]]}
            For each name, if len(dict[name]) > 1, we check each i > 0 in dict[name] 
            compare dict[name][0] until no more megre. 
            
        corner case check: 
        input: [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
        '''
        
        # step 1: set up dict for {name: [emails], ....}
        merge = {accounts[0][0]: [set(accounts[0][1:])]}
        for i in range(1, len(accounts)):
            name, new_account = accounts[i][0], set(accounts[i][1:])            
            if name not in merge:
                merge[name] = [set(accounts[i][1:])]
            else:
                j, union = 0, False
                while j < len(merge[name]) and union == False:  # once union happens, move
                    union = self.isSameSet(merge[name][j], new_account)
                    if union:
                        merge[name][j] = merge[name][j].union(new_account) # update union

                    j += 1

                if not union:
                    merge[name].append(new_account)
                
            
        # step 2: check if there is merge needed in dict within same name.
        for name in merge:
            union = True
            while union and len(merge[name]) > 1: 
                union, i = False, 1
                while not union and i < len(merge[name]):
                    union = self.isSameSet(merge[name][0], merge[name][i])
                    if union:
                        merge[name][0] = merge[name][0].union(merge[name][i])
                        merge[name].remove(merge[name][i])
                    else:
                        i += 1       
        
        output = []
        for name in merge:
            for i in range(len(merge[name])):
                output.append([name]+sorted(merge[name][i]))
        
        return output
    
    
    def isSameSet(self, set1, set2):
        '''
        check if set1 and set2 have common elements 
        '''
        union_set = set1.union(set2)
        if len(union_set) < len(set1) + len(set2):
            return True
        else:
            return False