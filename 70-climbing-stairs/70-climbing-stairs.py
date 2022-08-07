class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a = [0]*n
        a[n-1] = 1
        a[n-2] = 1
        for i in range(n-3,-1,-1):
            a[i] = a[i+1]+a[i+2]
        return a[0]+a[1]