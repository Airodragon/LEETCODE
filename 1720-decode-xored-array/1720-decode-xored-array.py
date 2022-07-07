class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            ans.append(i^first)
            first = i^first
        return ans