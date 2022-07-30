class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a = s.count(letter)
        return int((a/len(s))*100)