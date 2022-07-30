from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = []
        co = Counter(arr)
        for i in arr:
            if co[i]==1:
                a.append(i)
        if k>len(a):
            return ""
        return a[k-1]