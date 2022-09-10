class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def m(nums):
            nums.sort()
            mi = float('+inf')
            for i in nums:
                if i<mi and i!=0:
                    mi = i
            return mi
        count = 0
        while nums.count(0)!=len(nums):
            temp = m(nums)
            a = []
            for i in nums:
                if i!=0:
                    a.append(i-temp)
                else:
                    a.append(0)
            count+=1
            nums = a
        return count