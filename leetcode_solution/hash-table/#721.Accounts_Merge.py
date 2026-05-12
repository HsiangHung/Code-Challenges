#  721. Accounts Merge (medium)
#  https://leetcode.com/problems/accounts-merge/
#
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
        
        # step 1: set up dict for {name: [emails], ....} and also scan if union
        name_dict = {} 
        for account in accounts:
            name, emails = account[0], set(account[1:])   # trick, even from questions, repeated emails
            if name not in name_dict:
                name_dict[name] = [emails]
            else:
                i, union = 0, False
                while not union and i <= len(name_dict[name])-1:  # once union happens, move
                    if self.isUnion(name_dict[name][i], emails):
                        name_dict[name][i] = name_dict[name][i].union(emails) # update union
                        union = True
                    else:
                        i += 1
                if not union: name_dict[name].append(emails)


        ans = []
        # step 2: check if there is merge needed in dict within same name.
        for name in name_dict:
            emails = name_dict[name][:]
                        
            merge = True
            while merge and len(emails) > 1:
                merge = False
                i, merge = 1, False
                while not merge and i <= len(emails)-1:
                    if self.isUnion(emails[0], emails[i]):
                        emails[0] = set(emails[0]).union(emails[i])
                        emails.pop(i)
                        merge = True
                    else:
                        i += 1
        
            for x in emails:
                ans.append([name] + sorted(list(x)))
                
        return ans

    
    def isUnion(self, a, b):
        ''' check if set1 and set2 have common elements '''
        union_set = a.union(b)
        return True if len(union_set) < len(a) + len(b) else False
  
