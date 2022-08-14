class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        a = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        a.append([i,j,k])
        return len(a)