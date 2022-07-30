class Solution:
    def squareIsWhite(self, c: str) -> bool:
        a = int(c[1])%2
        b = ord(c[0])%2
        return not a==b