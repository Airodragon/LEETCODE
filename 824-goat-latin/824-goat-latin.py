class Solution:
    def toGoatLatin(self, t: str) -> str:
        s = ""
        temp = t.split(" ")
        for i in range(0,len(temp)):
            if temp[i][0].lower()=="a" or temp[i][0].lower()=="e" or temp[i][0].lower()=="i" or temp[i][0].lower()=="o" or temp[i][0].lower()=="u":
                s+=temp[i]+"ma"
            else:
                s+=temp[i][1:]+temp[i][0]+"ma"
            s+="a"*(i+1)+" "
        return s[:-1]