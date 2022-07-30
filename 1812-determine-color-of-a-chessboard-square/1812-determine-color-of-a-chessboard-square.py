class Solution:
    def squareIsWhite(self, c: str) -> bool:
        a,b = int(c[1])%2,ord(c[0])%2
        return not a==b