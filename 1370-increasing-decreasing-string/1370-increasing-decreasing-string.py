from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        counts = sorted(Counter(s).items())
        res = []
        reverse = False
        while len(res) != len(s):
            for i in range(len(counts)):
                i = -i - 1 if reverse else i
                char, count = counts[i]
                if count == 0:
                    continue
                res.append(char)
                counts[i] = (char, count - 1)
            reverse = not reverse

        return "".join(res)