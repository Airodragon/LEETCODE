class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(0,len(nums)):
            x.append(nums[nums[i]])
        return x