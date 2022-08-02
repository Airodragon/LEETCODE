class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            a = []
            temp = []
            for i in s:
                temp.append(int(i))
            # print(temp)
            for i in range(0,len(temp),k):
                a.append(temp[i:i+k])
            sum_array = []
            for i in a:
                sum_array.append(sum(i))
            # print(sum_array)
            s = ""
            for i in sum_array:
                s+=str(i)
            # print(s)
        return s
            
                