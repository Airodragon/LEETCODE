class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def substrings(s):
            a = []
            for i in range(0,len(s)):
                for j in range(i+1,len(s)+1):
                    a.append(s[i:j])
            return a
        a = substrings(s)
        # print(a)
        longest_l = float('-inf') 
        longest_s = ""
        for i in a:
            flag = True
            for j in i:
                if j.swapcase() not in i:
                    flag = False
            if flag and len(i)>longest_l:
                longest_l = len(i)
                longest_s = i
        return longest_s
                