class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dics = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    dics.append((i,j))    
        return len(dics)