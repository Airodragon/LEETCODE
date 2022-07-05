class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = set()
        for i in s:
            if i.swapcase() in s:
                ans.add(i)
        if len(ans)==0:
            return ""
        ans =  sorted(ans,reverse=True)
        # print(ans)
        return ans[0].upper()