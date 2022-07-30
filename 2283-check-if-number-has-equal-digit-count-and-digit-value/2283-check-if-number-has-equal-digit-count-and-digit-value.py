class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(0,len(num)):
            if int(num[i])!=num.count(str(i)):
                return False
        return True