class Solution:
    def numTrees(self, n: int) -> int:
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)
        return (fact(2*n))//(fact(n+1)*fact(n))