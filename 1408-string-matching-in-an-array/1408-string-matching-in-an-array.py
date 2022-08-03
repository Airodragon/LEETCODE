class Solution:
    def stringMatching(self, nums: List[str]) -> List[str]:
        a = set()
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] in nums[j] and i!=j:
                    a.add(nums[i])
        return a