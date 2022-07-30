class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(0,len(s)-1,2):
            ans += s[i] + chr(ord(s[i]) + int(s[i+1]))
        if(len(s)%2!=0):
            ans+=s[len(s)-1]
        return ans