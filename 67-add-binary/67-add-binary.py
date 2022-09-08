class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if int(a)==int(b) and int(b)==0:
            return "0"
        if int(a)==0:
            return b
        if int(b)==0:
            return a
        def binarytoDecimal(n):
            pow = 0
            ans = 0
            x = str(n)
            for i in x[::-1]:
                ans+=int(i)*(2**pow)
                pow+=1
            return ans
        def decimaltoBinary(n):
            a = ""
            while n>=2:
                r = n%2
                a+=str(r)
                n//=2
            if n==1:
                a+="1"
            return a[::-1]
        a_d = binarytoDecimal(a)
        b_d = binarytoDecimal(b)
        print(a_d)
        print(b_d)
        s_d = a_d +b_d
        print(s_d)
        return decimaltoBinary(s_d)
        