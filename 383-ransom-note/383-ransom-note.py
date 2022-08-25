class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(0,len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            idx = magazine.index(ransomNote[i])
            magazine=magazine[:idx]+magazine[idx+1:]
        return True