class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        first,second = 0,0 #0 steps require for 0th and 1st steps 
        
        for i in range(2,n+1):
            temp = min(second+cost[i-1]  , first +cost[i-2])
            first = second
            second = temp
        return second