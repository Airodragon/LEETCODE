class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = []
        for i in range(len(s)):
            ans.append((indices[i],s[i]))
        ans = sorted(ans)
        st = ""
        for i in ans:
            st+=i[1]
        return st