class Solution:
    def maximumUnits(self, box: List[List[int]], truckSize: int) -> int:
        for i in box:
            i[0],i[1]=i[1],i[0]
        box.sort(reverse=True)
        count = 0
        # print(box)
        for i in box:
            if truckSize==0:
                break
            while(i[1]!=0 and truckSize!=0):
                count+=i[0]
                i[1]-=1
                truckSize-=1
        # print(count)
        return count