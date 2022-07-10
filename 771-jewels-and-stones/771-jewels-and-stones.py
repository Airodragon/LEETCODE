class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_count = Counter(jewels)
        stone_count = Counter(stones)
        for i in stone_count:
            if i in jewels_count:
                count+=stone_count[i]
        return count