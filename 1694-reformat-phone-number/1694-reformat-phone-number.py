class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","")
        number = number.replace("-","")
        ans = ""
        while(len(number)>4):
            ans+=number[:3]+"-"
            number = number[3:]
        if(len(number)==3 or len(number)==2):
            ans+=number
            return ans
        else:
            ans+=number[:2]+"-"+number[2:]
            return ans