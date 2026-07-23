class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        ans= defaultdict(int)

        for i in s:
            ans[i]+=1

        for i in t:
            if ans[i] != 0 :
                ans[i]-=1
            else:
                return False
        return True