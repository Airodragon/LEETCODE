class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dic = []
        for i in arr:
            dic.append([i,1])
        for i in range(1,len(dic)):
            total = dic[i][1]
            for j in range(0,i):
                if dic[i][0]%dic[j][0]==0 and dic[i][0]//dic[j][0] in arr:
                    temp = arr.index(dic[i][0]//dic[j][0])
                    total +=  dic[j][1]*dic[temp][1]
            dic[i][1] = total
        sum1 = 0
        # print(dic)
        for i,j in dic:
            sum1+=j
        return sum1%((10**9)+7)
                    