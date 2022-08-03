class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li = sentence.split(" ")
        l = len(searchWord)
        for i in li:
            if i[:l]==searchWord:
                return li.index(i)+1
        return -1
            