class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[] # pair(index, height)
        maxarea= 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h :
                
                prevind,prevht = stack.pop()
                maxarea = max(maxarea , (i - prevind)* prevht )
                start = prevind
            stack.append([start,h])
        for i, h in stack :
            maxarea= max(maxarea,(len(heights)-i)* h)
        return maxarea