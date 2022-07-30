class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        temp = a[s[0]]
        for i in a:
            if a[i]!=temp:
                return False
        return True