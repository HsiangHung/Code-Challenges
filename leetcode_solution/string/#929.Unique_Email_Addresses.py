# 
# 929. Unique Email Addresses
#
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        email_set = set({})
        for i in range(len(emails)):
            local, domain = emails[i].split("@")

            i = 0
            local_ls = []
            while i < len(local) and local[i] != "+":
                if local[i] != ".":
                    local_ls.append(local[i])
                i += 1
            
            local = "".join(local_ls)
            email_set.add(local + "@" + domain)
        
        return len(email_set)
