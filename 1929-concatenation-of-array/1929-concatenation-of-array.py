class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = nums 
        x.extend(nums)
        return x