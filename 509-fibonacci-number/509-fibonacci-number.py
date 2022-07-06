class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibnocci(n-1)+self.fibnocci(n-2)
        
    def fibnocci(self,n):
        if n == 0:
            return 0 
        elif n == 1 or n == 2:
            return 1

        else:
            return self.fibnocci(n-1) + self.fibnocci(n-2)
