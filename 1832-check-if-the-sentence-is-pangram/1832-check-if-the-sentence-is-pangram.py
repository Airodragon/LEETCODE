class Solution:
    def checkIfPangram(self, s: str) -> bool:
        if len(s)<26:
            return False
        l = ['a','b','c',
             'd','e','f',
             'g','h','i',
             'j','k','l',
             'm','n','o',
             'p','q','r',
             's','t','u',
             'v','w',
             'x','y','z']
        for i in l:
            if i not in s:
                return False
        return True