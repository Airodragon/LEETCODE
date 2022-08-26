class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        x = bin(n).replace("0b", "")
        return x.count('1')==1