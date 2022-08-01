class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a = []
        for i in range(0,len(s)):
            if s[i]==c:
                a.append(i)
        x = []
        for i in range(0,len(s)):
            temp = []
            for j in a:
                temp.append(abs(i-j))
            x.append(min(temp))
        return x