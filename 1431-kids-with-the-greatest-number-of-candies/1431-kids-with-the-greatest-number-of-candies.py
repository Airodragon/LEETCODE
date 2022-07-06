class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in candies:
            temp = i + extraCandies
            ans.append(temp>=max(candies))
        return ans