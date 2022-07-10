class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = 0
        sum_nums = sum(nums)
        left_sum = 0
        right_sum = sum_nums
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum==right_sum:
                return i
            left_sum += nums[i]
        return -1
            