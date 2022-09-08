class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i,j in items1:
            d[i] = j
        for x,y in items2:
            if x in d:
                d[x]+=y
            else:
                d[x] = y
        ans = []
        for i in sorted(d):
            ans.append([i,d[i]])
        return ans