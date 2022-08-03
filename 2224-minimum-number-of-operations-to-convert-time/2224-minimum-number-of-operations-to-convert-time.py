class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        tdm = abs((int(current[:2])-int(correct[:2]))*60 + (int(current[3:])-int(correct[3:])))
        count = 0
        while tdm>=60:
            tdm-=60
            count+=1
        while tdm>=15:
            tdm-=15
            count+=1
        while tdm>=5:
            tdm-=5
            count+=1
        if tdm>0:
            count+=tdm
        return count