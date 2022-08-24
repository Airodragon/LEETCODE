class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        # flag = True
        while(n>3):
            # print(n)
            n/=3
        n = n%3
        return n==0