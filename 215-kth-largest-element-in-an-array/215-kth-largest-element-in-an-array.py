class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = set(nums)
        # nums = sorted(nums)
        nums.sort()
        return nums[len(nums)-k]