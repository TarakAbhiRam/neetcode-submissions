class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxprof= 0 
        for i in range(len(prices)):
            mini = min(mini,prices[i])
            maxprof = max(maxprof, prices[i]-mini)
        return maxprof
