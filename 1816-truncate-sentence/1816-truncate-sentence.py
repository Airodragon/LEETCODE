class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = s.split(' ')
        s = ""
        for i in range(0,k):
            s+=temp[i]+" "
        return s[:-1]