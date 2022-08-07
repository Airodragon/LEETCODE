class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = []
        def pascalTriangle(num):
            for n in range(0, num+1):
                temp = []
                for k in range(0, n + 1):
                    temp.append(fact(n,k))
                # temp = []
            return temp
        def findFact(i):
            if i == 1 or i == 0:
                return 1
            else:
                return i*findFact(i-1)
            
        def fact(n, k):
            return int(findFact(n)/(findFact(n-k)*findFact(k)))
        
        return pascalTriangle(rowIndex)