class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        temp = 0
        for i in key:
            if i!=' ' and i not in dic:
                dic[i]=char[temp]
                temp+=1
            if len(dic)==26:
                break
        # print(dic)
        result = ""
        for i in message:
            if i==' ':
                result+=" "
            else:
                result+=dic[i]
        return result