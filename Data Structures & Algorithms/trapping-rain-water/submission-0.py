class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right =[0]*len(height)

        maxl = height[0]
        for i in range(len(height)):
            maxl= max(maxl,height[i])
            left[i] = maxl
        
        maxr = height[-1]
        for i in range(len(height)-1,-1,-1):
            maxr = max(maxr,height[i])
            right[i] = maxr
        
        water = 0
        for i in range(len(height)):
            water += min(left[i],right[i]) - height[i]
        return water
        
