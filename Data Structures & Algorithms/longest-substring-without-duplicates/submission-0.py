class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slide= set()
        left,longest = 0 ,0
        for i in range(len(s)):
            while s[i] in slide:
                slide.remove(s[left])
                left+=1
            slide.add(s[i])
            longest = max(longest,i-left+1)
        return longest
            
                
