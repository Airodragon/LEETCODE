class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        text = text.split(' ')
        for i in text:
            flag = False
            for j in brokenLetters:
                if j in i:
                    flag = True
            if not flag:
                count+=1
        return count