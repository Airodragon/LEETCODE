class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        sample  = Counter(arr1)
        ans = []
        for i in arr2:
            for j in range(sample[i]):
                ans.append(i)
        for i in arr1:
            if i not in ans:
                ans.extend([i]*sample[i])
        return ans