class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        a = []
        x = Counter(nums)
        for i in x:
            count+=(x[i]//2)
            a.append(x[i]%2)
        while 0 in a:
            a.remove(0)
        return[count,len(a)]