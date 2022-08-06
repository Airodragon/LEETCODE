class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        temp = []
        total_subsets = len(nums)**2
        subset = [0]*len(nums)
        def xor_finder(a):
            xor = 0
            for i in a:
                xor = xor ^ i
            return xor
        def helper(nums,subset,i):
            if i==len(nums):
                xor_value = xor_finder(subset)
                temp.append(xor_value)
            else:
                subset[i] = 0
                helper(nums,subset,i+1)
                subset[i] = nums[i]
                helper(nums,subset,i+1)
        helper(nums,subset,0)
        return sum(temp)
        