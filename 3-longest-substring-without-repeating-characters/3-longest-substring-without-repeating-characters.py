class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0
        for i in range(0,len(s)):
            count = 0
            ans = ""
            ans = ans + s[i]
            for j in range(i+1,len(s)):
                if s[j] not in ans:
                    ans = ans + s[j]
                else:
                    break
                # print(ans)
            sol = max(sol,len(ans))
        return sol