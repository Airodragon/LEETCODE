class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 0
        pos = 0
        while pos<len(s):
            temp = s[pos]
            count = 1
            # print(pos)
            while pos<len(s)-1 and s[pos+1]==s[pos]:
                count+=1
                pos+=1
                # print(pos)
            pos+=1
            max_count = max(count,max_count)
        return max_count