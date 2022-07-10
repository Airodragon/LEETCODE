class Solution:
       def pivotIndex(self, nums: List[int]) -> int:
        pivot_idx = 0
        sum_ = 0
        curr = 0
        sum_ = sum(nums)
        left_sum = 0
        right_sum = sum_
        for curr in range(len(nums)):
            right_sum -= nums[curr]
            if right_sum == left_sum:
                return curr
            left_sum += nums[curr]
        return -1