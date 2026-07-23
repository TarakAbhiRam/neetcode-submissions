class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*(len(nums) - k + 1)
        for i in range(len(nums)-k+1):
            ans[i] = (max(nums[i:i+k]))
        return ans
