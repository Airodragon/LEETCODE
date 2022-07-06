class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        ans = []
        for i in range(0,n):
            ans.append(x[i])
            ans.append(y[i])
        return ans