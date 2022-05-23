class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        su = 0
        for i in range(0,len(nums),2):
            s = [nums[i],nums[i+1]]
            su += min(s)
        return su