class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        a = []
        a.append(0)
        a.append(1)
        for i in range(2,n+1):
            if i%2==0:
                a.append(a[i//2])
            else:
                a.append(a[i//2] + a[(i//2)+1])
        # print(a)
        return max(a)