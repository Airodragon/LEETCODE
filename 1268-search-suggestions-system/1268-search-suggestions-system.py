class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        for i in range(0,len(searchWord)):
            temp = []
            for j in products:
                if j[:i+1]==searchWord[:i+1]:
                    temp.append(j)
            temp.sort()
            ans.append(temp[:3])
        return ans