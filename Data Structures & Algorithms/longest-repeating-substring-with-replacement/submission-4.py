class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        look = defaultdict(int)
        left,right = 0,0
        
        for i in range(len(s)):
            look[s[i]]+=1
            maxi = max(look.values())
            if  (right-left+1) - maxi <= k :
                res = max( res , right - left + 1)
            while (right-left+1) - maxi > k :
                look[s[left]]-=1
                left+=1
            right+=1
        return res

