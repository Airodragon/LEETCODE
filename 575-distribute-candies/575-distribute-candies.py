class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        x = set(candyType)
        if len(x)<n//2:
            return len(x)
        else:
            return n//2
            