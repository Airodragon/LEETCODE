class Solution:
    def convert(self, s: str, numRows: int) -> str:
        c,r,f,i = {i:[]  for i in range(numRows)},[],1,-1
        
        if numRows == 1:
            return s
        
        for l in s:
            if f == 1:
                i += 1
                c[i].append(l)

            else:
                i -= 1
                c[i].append(l)

            if i == numRows-1:
                f = 0
            elif i == 0 and f != 1:
                f = 1 
        
        for v in c.values():
            r += v
            
        return ("").join(r)