class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = text.split(" ")
        ans = []
        for i in range(0,len(s)-2):
            if s[i]==first and s[i+1]==second:
                ans.append(s[i+2])
        return ans