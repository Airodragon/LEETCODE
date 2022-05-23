class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sample = heights.copy()
        sample.sort()
        count = 0
        if sample==heights: return 0
        for i in range(0,len(heights)):
            if sample[i]!=heights[i]:
                count+=1
        return count