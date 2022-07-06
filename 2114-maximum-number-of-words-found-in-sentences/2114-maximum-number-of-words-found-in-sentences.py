class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for i in sentences:
            total_words = len(i.split(' '))
            max_word = max(max_word,total_words)
        return max_word