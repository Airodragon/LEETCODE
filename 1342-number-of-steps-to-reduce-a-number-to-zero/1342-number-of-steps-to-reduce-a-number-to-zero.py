class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while(num>0):
            if(num>0 and num%2==0):
                num/=2
                count+=1
            elif(num>0 and num%2!=0):
                num-=1
                count+=1
            else:
                break
        return count