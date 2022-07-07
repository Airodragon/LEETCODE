class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(index)):
            ans.insert(index[i],nums[i])
        return ans