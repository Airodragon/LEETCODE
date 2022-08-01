class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = len(strs[0])
        count = 0
        for i in range(l):
            temp = []
            for j in strs:
                temp.append(j[i])
            a = temp.copy()
            b = temp.copy()
            a.sort()
            if temp!=a:
                count+=1
        return count