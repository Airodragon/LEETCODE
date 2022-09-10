class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumd(n):
            s = 0
            for i in str(n):
                s+=int(i)
            return s
        a = {}
        for i in range(1,n+1):
            x = sumd(i)
            if x not in a:
                a[x] = 1
            else:
                a[x] = a[x] + 1
        maxi = float('-inf')
        for i in a:
            maxi = max(maxi,a[i])
        count = 0
        for i in a:
            if a[i]==maxi:
                count+=1
        return count