class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            x = nums[i]
            y = nums[i+1]
            while x>0:
                ans.append(y)
                x-=1
        return ans