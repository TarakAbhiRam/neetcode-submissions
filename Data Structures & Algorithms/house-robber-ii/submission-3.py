class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case containing only one element
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))


    def helper(self,nums:List[int])->int:
        rob1, rob2 = 0,0
        for i in nums:
            newrob = max(rob2,rob1+i)
            rob1 = rob2
            rob2 = newrob
        return rob2
        