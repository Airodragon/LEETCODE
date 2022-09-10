class Solution(object):
    def checkDistances(self, s, distance):
        arr = [0]*26
        for i in range(len(s)):
            if arr[ord(s[i]) - 97] != 0 and i - arr[ord(s[i]) - 97] != distance[ord(s[i]) - 97]:
                return False
            arr[ord(s[i]) - 97] = i+1
        return True