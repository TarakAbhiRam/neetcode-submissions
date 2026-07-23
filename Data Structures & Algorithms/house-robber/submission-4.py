class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        #max value until here

        for i in range(2,n):
            dp[i]= max(dp[i-1],dp[i-2]+nums[i])#if previous is better, 
            #carry forward
            #hence no cost
            #if cost there means we are using it
            #this bypasses if there are any even no of spaces
        return dp[-1]
