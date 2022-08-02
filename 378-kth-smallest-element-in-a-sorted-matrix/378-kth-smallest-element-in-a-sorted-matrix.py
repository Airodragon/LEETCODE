class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for i in matrix:
            a.extend(i)
        a.sort()
        print(a)
        return a[k-1]