class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        t = word[:idx+1]
        return t[::-1]+word[idx+1:]