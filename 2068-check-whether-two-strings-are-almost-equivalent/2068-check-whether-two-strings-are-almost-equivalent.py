class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        Counter_word1 = Counter(word1)
        Counter_word2 = Counter(word2)
        for i in Counter_word1:
            if i in Counter_word2 and abs(Counter_word2[i] - Counter_word1[i])>3:
                return False
            
            if i not in Counter_word2 and Counter_word1[i]>3:
                return False
        for i in Counter_word2:
            if i in Counter_word1 and abs(Counter_word1[i] - Counter_word2[i])>3:
                return False
            
            if i not in Counter_word1 and Counter_word2[i]>3:
                return False
        
        return True