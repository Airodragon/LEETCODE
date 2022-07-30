class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = ""
        b = ""
        c = ""
        dic = {'a':'0',
               'b':'1',
               'c':'2', 
               'd':'3',
               'e':'4',
               'f':'5',
               'g':'6',
               'h':'7',
               'i':'8',
               'j':'9'}
        for i in firstWord:
            a+=dic[i]
        for i in secondWord:
            b+=dic[i]
        for i in targetWord:
            c+=dic[i]
        return int(a)+int(b)==int(c)