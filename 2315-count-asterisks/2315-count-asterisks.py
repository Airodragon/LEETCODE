class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        flag = True
        for i in s:
            if i=='|':
                flag = not flag
            if i=='*' and flag:
                count+=1
        return count