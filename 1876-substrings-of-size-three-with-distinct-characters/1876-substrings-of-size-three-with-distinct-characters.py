class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        temp = []
        count = 0
        for i in range(0,len(s)-2):
            x = s[i:i+3]
            x_counter = Counter(x)
            flag = False
            for j in x_counter:
                if x_counter[j]!=1:
                    flag = True
            if not flag:
                count+=1
        return count    