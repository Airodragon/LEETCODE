class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = Counter(nums)
        for i in x:
            if x[i]==len(nums)//2:
                return i