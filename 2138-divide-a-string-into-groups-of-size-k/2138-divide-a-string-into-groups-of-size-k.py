class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a = []
        while len(s)>=k:
            a.append(s[:k])
            s = s[k:]
        if len(s)!=0:
            a.append(s+fill*(k-len(s)))
        return a
                