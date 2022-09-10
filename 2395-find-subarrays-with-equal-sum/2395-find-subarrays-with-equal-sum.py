class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        def subarray(arr):
            a = []
            for i in range(0,len(arr)-1):
                a.append([arr[i],arr[i+1]])
            return a
        x = subarray(nums)
        a = []
        for i in x:
            if sum(i) in a:
                return True
            else:
                a.append(sum(i))
        return False