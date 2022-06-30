import statistics
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # avg = sum(nums)//len(nums)
        avg = int(statistics.median(nums))
        moves = 0
        # print(avg)
        for i in nums:
            # print(abs(i-))
            moves+=abs(i-avg)
        # print(moves)
        return moves