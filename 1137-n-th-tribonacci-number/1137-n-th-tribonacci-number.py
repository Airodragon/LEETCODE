class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        t = [0,1,1]
        while len(t)<=n:
            # print(t[len(t)-3:len(t)])
            t.append(sum(t[len(t)-3:len(t)]))
        return t[-1]