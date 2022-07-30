class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = []
        for i in s:
            if i in a:
                return i
            else:
                a.append(i)