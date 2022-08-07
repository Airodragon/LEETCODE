class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        i = 0
        count = 0
        for h in t:
            if h==s[i]:
                count+=1
                i+=1
                if i==len(s):
                    return True
        return count==len(s)