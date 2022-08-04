import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        e,r = q,p
        while(e%2==0 and r%2==0):
            e//=2
            r//=2
        if(e%2==0 and r%2!=0):
            return 0
        if(e%2!=0 and r%2==0):
            return 2
        if(e%2!=0 and r%2!=0):
            return 1