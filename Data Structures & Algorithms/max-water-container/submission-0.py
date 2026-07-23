class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        Water= 0
        while l < r:
            minht = min(heights[l],heights[r])
            area = (r-l)*minht
            Water=max(area,Water)
            if heights[l]==minht:
                l+=1
            else:
                r-=1
        return Water