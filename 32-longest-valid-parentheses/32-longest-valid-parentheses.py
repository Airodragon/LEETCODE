class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for ind, char in enumerate(s):
            if char == '(':
                stack.append(ind)
            else:
                stack.pop()
                if not stack:
                    stack.append(ind)
                else:
                    max_len = max(max_len, ind-stack[-1])
        return max_len