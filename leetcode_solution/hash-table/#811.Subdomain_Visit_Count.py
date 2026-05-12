#  811. Subdomain Visit Count (easy)
#  https://leetcode.com/problems/subdomain-visit-count/
#
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain_dict = {}
        for domain in cpdomains:
            domain = domain.split(" ")
            times, domain = int(domain[0]), domain[1].split(".")
            for i in range(len(domain)):
                domain_dict[".".join(domain[i:])] = domain_dict.get(".".join(domain[i:]), 0) + int(times)
                            
        return [str(domain_dict[x])+" "+x for x in domain_dict]