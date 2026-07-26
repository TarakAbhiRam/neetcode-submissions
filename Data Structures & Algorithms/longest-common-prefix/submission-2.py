class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]
            
        strs.sort()
        
        maxpre = ""
        for i in range(len(strs)-1):
            cnt = 0
            pre = ""
            while cnt < len(strs[i]) and cnt < len(strs[i+1]):
                if strs[i][cnt] != strs[i+1][cnt]:
                    break
                pre += strs[i][cnt]
                cnt += 1
            if i == 0 or len(pre) < len(maxpre):
                maxpre = pre
        return maxpre

            
            
