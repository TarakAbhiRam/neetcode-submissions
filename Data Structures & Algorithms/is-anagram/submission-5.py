class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        
        for i in s:
            seen[i] = seen.get(i,0)+1

        for i in t:
            if i not in seen:
                return False
            seen[i]-=1
            if (seen[i]<0):
                return False
        return True