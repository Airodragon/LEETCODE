class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ans = []
        for i in nums:
            ans.append(i+sum)
            sum+=i
        return ans