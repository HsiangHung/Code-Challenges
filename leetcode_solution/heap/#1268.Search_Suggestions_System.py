#
# 1268. Search Suggestions System
#
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products = sorted(products) # lexicographical order

        res = []
        for i in range(1, len(searchWord)+1):
            w = searchWord[:i]

            ans = []
            for j in range(len(products)):
                if products[j][:i] == w:
                    ans.append(products[j])
                    if len(ans) >= 3:
                        break

            res.append(ans)

        return res