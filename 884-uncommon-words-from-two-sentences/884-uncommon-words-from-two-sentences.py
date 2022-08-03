class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1+" "+s2
        l = s1.split(" ")
        Count_l = Counter(l)
        ans = []
        for i in Count_l:
            if Count_l[i]==1:
                ans.append(i)
        return ans